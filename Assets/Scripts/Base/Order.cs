using UnityEngine;
using System.Collections;

public abstract class Order {
	readonly public Human orderer;
	readonly public Human orderee;
	public Order (Human orderer, Human orderee) {
		if (orderee.IsSubordinateOf(orderer)) {
			this.orderer = orderer;
			this.orderee = orderee;
		} else {
			throw new System.InvalidOperationException("Not subordinate");
		}
	}

	abstract public void execute();
}

public class FollowOrder: Order {
	private Human follower;
	private Human followee;
	public FollowOrder(Human orderer, Human orderee): base(orderer, orderee) {
		follower = orderee;
		followee = orderer;
	}

	public override void execute() {
		Debug.Log("followed");
		follower.FollowHuman(followee);
	}
}