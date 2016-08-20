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
}
