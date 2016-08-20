using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class Group {
	private static int idCount = 1;
	private int level = 1;
	public readonly int id;
	protected Dictionary<int, Human> members = new Dictionary<int, Human>();
    protected Dictionary<int, Group> subteams = new Dictionary<int, Group>();
	private Human leader;
	public readonly string name;


	public Group() {
		id = idCount++;
	}

	public Group(Human member) {
		id = idCount++;
		AddMember(member);
	}

	public void AddMember(Human member) {
		if (members.Count == 0) {
			leader = member;
		}

		members.Add(member.id, member);
		AssignLeader();
		Plan();
	}

	public void AssignLeader() {
		foreach(KeyValuePair<int, Human> entry in members) {
			Human member = entry.Value;
            if (member.tag == "Player") {
				leader = member;
				return;
			}
		}
	}

	public void Plan() {
		Human preMember = leader;

        foreach(KeyValuePair<int, Human> entry in members) {
			Human member = entry.Value;
            if (member != leader) {
				member.FollowHuman(preMember);
				preMember = member;
			}
		}
	}
}
