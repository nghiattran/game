using UnityEngine;
using System.Collections;
using System;

public class Nationality {
	public readonly string [] firstNames;
	public readonly string [] lastNames;
	public readonly string name;
	private System.Random rand = new System.Random();
	public Nationality() {
		// Default constructor should not be used
		// throw;
	}

	public Nationality(string name, string [] firstNames, string [] lastNames) {
		this.name = name;
		this.firstNames = firstNames;
		this.lastNames = lastNames;
	}

	public string GenerateName() {
		return RandomFirstName() + " " + RandomLastName();
	}

	public string RandomFirstName() {
		return firstNames[rand.Next(0, firstNames.Length)];
	}

	public string RandomLastName() {
		return lastNames[rand.Next(0, lastNames.Length)];
	}
}

public class Vietnam: Nationality {
	public static readonly string[] firstNames = new string[] {"Nghia", "Kha", "Thuc"};
	public static readonly string[] lastNames = new string[] {"Tran", "Nguyen", "Le"};
	public static readonly string name = "Vietnam";
	
	public Vietnam(): base(name, firstNames, lastNames) {
		
	}
}
