using UnityEngine;
using System.Collections;
using System;

public class Nationality {
	public readonly string [] firstNames;
	public readonly string [] lastNames;
	public readonly string name;
	private static readonly System.Random random = new System.Random();
	private static readonly object syncLock = new object();

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
		return firstNames[RandomNumber(0, firstNames.Length)];
	}

	public string RandomLastName() {
		return lastNames[RandomNumber(0, lastNames.Length)];
	}

	public static int RandomNumber(int min, int max) {
		lock(syncLock) { // synchronize
			return random.Next(min, max);
		}
	}
}

public class Vietnam: Nationality {
	public static readonly string[] firstNames = new string[] {"1", "2", "3", "4", "5", "6", "7"};
	public static readonly string[] lastNames = new string[] {"Tran", "Nguyen", "Le"};
	public static readonly string name = "Vietnam";
	
	public Vietnam(): base(name, firstNames, lastNames) {
		
	}
}

