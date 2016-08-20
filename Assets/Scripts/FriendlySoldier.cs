using UnityEngine;
using System.Collections;

public class FriendlySoldier : Soldier {
	public FriendlySoldier():base(new Vietnam()) {
		
	}

	// Use this for initialization
	void Start () {
		base.Start();
		
		Soldier[] soldiers = FindObjectsOfType(typeof(Soldier)) as Soldier[];
        foreach (Soldier soldier in soldiers) {
			if (soldier is Player) {
				JoinGroup(soldier);
			}
        }

		AddAction(new CheckAction(this, "e"));
	}
}
