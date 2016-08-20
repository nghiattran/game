using UnityEngine;
using System.Collections;

public class Player : Soldier {
	public Player(): base(new Vietnam()) {

	}

	// Use this for initialization
	protected void Start () {
		base.Start();
		Debug.DrawLine(new Vector3(200,200,200), Vector3.zero, Color.green, 2, false);
	}
	
	// Update is called once per frame
	protected override void PreUpdate () {
		HandleMovement();
		LookAtMouse();


		// if (Input.GetMouseButtonDown(0)) {
        // 	target = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        // 	target.z = transform.position.z;
        // }
		// MoveTo(target);
	}

	private void HandleMovement() {
		float horizontal = Speed(Input.GetAxis("Horizontal"));
		float vertical = Speed(Input.GetAxis("Vertical"));
		
		myRigidBody.velocity = new Vector2(horizontal * movementSpeed, vertical * movementSpeed);

	}

	private void LookAtMouse() {
		LookAt(Input.mousePosition);
	}

	private float Speed(float axis) {
		if (axis != 0) {
			return 0.3f * Mathf.Sign(axis);
		}
		return axis;
	}

	private void Flip () {
		Vector2 target = new Vector2(Input.mousePosition.x, Input.mousePosition.y);
		target = Camera.main.ScreenToWorldPoint (new Vector2 (target.x, target.y));
		float lookRight = target.x - myRigidBody.position.x;
		if ((lookRight > 0 && !isFacingRight) || (lookRight < 0 && isFacingRight)) {
			isFacingRight = !isFacingRight;
			Vector3 theScale = transform.localScale;
			theScale.x *= -1;
			transform.localScale = theScale;
		}
	}
}
