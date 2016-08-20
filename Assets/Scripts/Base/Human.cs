using UnityEngine;
using System.Collections;
using System.Collections.Generic;


public abstract class BaseHuman : MonoBehaviour {
	readonly public int id;
	public readonly string charName;

	private static int idCount = 1;
	// -2 means independent
	private int teamId = -1;

	public BaseHuman (Nationality naltionality) {
		id = idCount++;
		charName = naltionality.GenerateName();
	}

	abstract protected void Update();

	public int GetTeamId() {
		return teamId;
	}
}

public abstract class Human : BaseHuman {
	protected Rigidbody2D myRigidBody;
	protected bool isFacingRight = true;
	protected Vector3 target;
	protected Human followee;
	protected Human leader;
	protected Dictionary<int, Human> subordinates = new Dictionary<int, Human>();
	private Rect rect;
 	private Vector3 offset;

	[SerializeField]
	protected float movementSpeed;

	public Human(Nationality naltionality): base(naltionality) {
		rect = new Rect(0, 0, charName.Length * 10, 20);
		offset = new Vector3(- charName.Length * 0.08f, 0.2f);
	}

	// Use this for initialization
	protected void Start () {
		myRigidBody = GetComponent<Rigidbody2D>();
		
		// Disable rotation 
		myRigidBody.freezeRotation = true;
	}

	protected void MoveTo(Vector3 target) {
		transform.position = Vector3.Lerp(transform.position, target, movementSpeed * Time.deltaTime);
	}

	protected void UnFollow() {
		followee = null;
	}

	public void FollowHuman(Human followee) {
		this.followee = followee;
	}
	
	private void OnGUI(){
		Vector2 point = Camera.main.WorldToScreenPoint(transform.position + offset);
		rect.x = point.x;
		rect.y = Screen.height - point.y - rect.height;
		GUI.Label(rect, charName);
	}

	protected sealed override void Update() {
		PreUpdate();
		

		if (this.followee != null) {
			Follow(followee);
		}
		
		PostUpdate();
	}

	private void Follow(Human followee) {
		Vector3 target = followee.GetPosition();
		float distance = Vector3.Distance(target, transform.position);
		
		if (distance > 1) {
			MoveTo(target);
		}
	}

	public Vector3 GetPosition() {
		return transform.position;
	}

	virtual protected void PreUpdate() {
		
	}

	virtual protected void PostUpdate() {
		
	}

	protected void SetLeader(Human leader) {
		this.leader = leader;
		leader.SetSubordinate(this);
	}

	protected void RemoveLeader() {
		this.leader = null;
	}

	public void SetSubordinate(Human subordinate) {
		subordinates.Add(subordinate.id, subordinate);
		Plan(subordinate);
		// foreach(KeyValuePair<int, Human> entry in subordinates) {
		// 	Debug.Log(entry.Key);
		// }
	}

	protected void RemoveSubordinate(Human subordinate) {
		subordinates.Remove(subordinate.id);
		Plan(subordinate);
	}

	private void Plan(Human subordinate) {
		Order newOrder = new FollowOrder(this, subordinate);
		GetOrder(subordinate, newOrder);
	}

	private void GiveOrder(Human subordinate, Order order) {

	}

	public void GetOrder(Human leader, Order order) {
		order.execute();
	}

	public bool IsSubordinateOf(Human ahuman) {
		if (ahuman == leader) {
			return true;
		}
		return false;
	}

	protected void LookAt (Vector3 target) {
		target = target - Camera.main.WorldToScreenPoint(transform.position);
		float angle = Mathf.Atan2(target.y, target.x) * Mathf.Rad2Deg;
		transform.rotation = Quaternion.AngleAxis(angle, Vector3.forward);
		Debug.DrawLine(transform.position, target, Color.green, 2, false);
	}
}