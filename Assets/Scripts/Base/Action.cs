using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

public abstract class ActionBase {
	protected readonly Human character;

	public ActionBase(Human character) {
		this.character = character;
	}

	abstract public void Execute();
}

public abstract class Action {
	protected readonly Human character;

	public Action(Human character) {
		this.character = character;
	}

	abstract public void Execute();
	abstract public void ExecuteUpdate();
	abstract public void ExecuteRate();
}

class FollowAction: Action {
	private readonly Human followee;
	private Vector3 location; 

	public FollowAction(Human character, Human followee): base(character) {
		this.followee = followee;
		location = GetDestination();
	}

	public override void Execute() {
		// location = GetDestination();
	}

	public override void ExecuteUpdate() {
		float distance = Vector3.Distance(location, character.GetPosition());
		Debug.Log(location.x + " " + location.y);
		if (distance > 1.5) {
			character.MoveTo(location);
		}
	}

	public override void ExecuteRate() {
		location = GetDestination();
	}

	private Vector3 GetDestination() {
		Vector3 newLocation = followee.GetPosition();
		float distance = Vector3.Distance(location, newLocation);
		if (distance > 0.5) {
			return newLocation;
		}
		return followee.GetPosition();
	}
}

class WatchAction: Action {
	private readonly Vector3 location;
	public WatchAction(Human character, Vector3 location): base(character) {
		this.location = location;
	}

	public override void ExecuteUpdate() {}
	public override void Execute() {
		character.LookAtWorld(location);
	}
	public override void ExecuteRate(){}
}

class CheckAction: Action {
	// east, west south, north
	private readonly string acceptableDirections = "ewsn"; 
	private readonly List<char> directions = new List<char>();
	
	public CheckAction(Human character, string directions): base(character) {
		foreach(char c in directions){
			if (acceptableDirections.Contains(c) && this.directions.Contains(c)) {
				this.directions.Add(c);
			}
		}
	}
	
	public override void ExecuteUpdate() {}
	public override void Execute() {
		character.Check();
	}
	public override void ExecuteRate(){}
}
