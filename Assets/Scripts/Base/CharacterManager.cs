using UnityEngine;
using System.Collections;
using System;

public sealed class CharacterManager {
   private static volatile CharacterManager instance;
   private static object syncRoot = new UnityEngine.Object();

   private CharacterManager() {}

   public static CharacterManager Instance {
      get  {
         if (instance == null)  {
            lock (syncRoot)  {
               if (instance == null) 
                  instance = new CharacterManager();
            }
         }

         return instance;
      }
   }

   
}