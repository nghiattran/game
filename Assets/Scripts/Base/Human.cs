using UnityEngine;
using System.Collections;
using System.Collections.Generic;


public abstract class BaseHuman : MonoBehaviour {
	readonly public int id;
	public readonly string charName;

	private static int idCount = 1;
	protected Group myGroup = null;
	private int teamId = -1;

	public BaseHuman (Nationality naltionality) {
		id = idCount++;
		charName = naltionality.GenerateName();
	}

	abstract protected void Update();

	public int GetGroupId() {
		return myGroup.id;
	}

	public Group GetGroup() {
		return myGroup;
	}
}

public abstract class Human : BaseHuman {
	public Rigidbody2D myRigidBody;
	private Rect rect;
 	private Vector3 offset;
	private List<Action> actions = new List<Action>();
	
	[SerializeField]
	public float movementSpeed;

	public Human(Nationality naltionality): base(naltionality) {
		// Need to be in constructor since at this time charName is already generated
		rect = new Rect(0, 0, charName.Length * 10, 20);
		offset = new Vector3(- charName.Length * 0.08f, 0.2f);
	}

	// Use this for initialization
	protected void Start () {
		myRigidBody = GetComponent<Rigidbody2D>();
		
		// Disable rotation 
		myRigidBody.freezeRotation = true;

		InvokeRepeating("OncePerSecond", 0.0f, 1.0f);
		InvokeRepeating("TenPerSecond", 0.0f, 0.03f);
	}

	public void MoveTo(Vector3 target) {
		transform.position = Vector3.MoveTowards(transform.position, target, 0.4f * movementSpeed * Time.deltaTime);
	}

	public void FollowHuman(Human followee) {
		actions.Add(new FollowAction(this, followee));
	}

	public void JoinGroup(Group aGroup) {
		myGroup = aGroup;
		myGroup.AddMember(this);
	}

	public void JoinGroup(Human aHuman) {
		aHuman.AddMember(this);
	}

	public void AddMember(Human aHuman) {
		if (myGroup == null) {
			myGroup = new Group(this);
		}
		myGroup.AddMember(aHuman);
	}
	
	private void OnGUI(){
		Vector2 point = Camera.main.WorldToScreenPoint(transform.position + offset);
		rect.x = point.x;
		rect.y = Screen.height - point.y - rect.height;
		GUI.Label(rect, charName);
	}

	protected sealed override void Update() {
		PreUpdate();
		
		foreach (Action action in actions) {
			action.ExecuteUpdate();
        }
		
		PostUpdate();
	}

	private void OncePerSecond() {
		foreach (Action action in actions) {
			action.Execute();
        }
	}

	private void TenPerSecond() {
		foreach (Action action in actions) {
			action.ExecuteRate();
        }
	}

	public void Follow(Human followee) {
		Vector3 target = followee.GetPosition();
		float distance = Vector3.Distance(target, transform.position);
		
		if (distance > 1.5) {
			MoveTo(target);
		}
	}

	public Vector3 GetPosition() {
		return transform.position;
	}

	virtual protected void PreUpdate() {}

	virtual protected void PostUpdate() {}

	public void Check() {
		float xCoor = 0.707f;
		float yCoor = UnityEngine.Random.Range(-xCoor, xCoor);
		Vector3 location = new Vector3(xCoor, yCoor, -10) + transform.position;
		LookAtWorld(location);
	}

	public void WatchLocation(Vector3 target) {
		actions.Add(new WatchAction(this, target));
	}

	public void AddAction(Action action) {
		actions.Add(action);
	}

	public void LookAt (Vector3 target) {
		target = target - Camera.main.WorldToScreenPoint(transform.position);
		RotateTo(target);
	}

	public void LookAtWorld (Vector3 target) {
		target = target - transform.position;
		RotateTo(target);
	}

	protected void RotateTo (Vector3 target) {
		float angle = Mathf.Atan2(target.y, target.x) * Mathf.Rad2Deg;
		Rotate(angle);
	}

	protected void Rotate (float angle) {
		transform.rotation = Quaternion.AngleAxis(angle, Vector3.forward);
		// transform.Rotate(new Vector3(0, 0, angle) * Time.deltaTime);
	}
}