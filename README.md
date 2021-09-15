This is a game for two player. It involves the purchasing of different kinds of units to create an army in order to battle the army against another player until a victor is produced. The armies can be arranged in different formations, and each player are given certain amount of money to purchase a variety of units. 

Unit Types: 
![image](https://user-images.githubusercontent.com/67167072/133466013-8a37f94c-f16e-4a6c-8100-79a9b9b381c0.png)

- Fighter indicates the kind of fighter unit 
- Life indicates the starting number of life points 
- Exp indicates the starting number of experience points 
- Speed indicates the expression used to compute its speed (which may be negative)
- Damage on attack indicates the expression used to compute the damage it inflicts on attack 
- Lost life after defence indicates the expression used to compute the amount of life a unit loses after defending 
- Cost indicates theamount of money needer to buy such a unit

**RULE**

ORDERING:
After buying units, the units in the army of each of player is ordered as follow: 
  Soldiers -> Archers -> Cavalry 
This means Soldiers will battle first, then Archers, and finally the Cavalry 

COMBAT INSTRUCTION:
Battling involves attacking and defending, after which life is lost according to the **Damage on attack** stat and the **Lost life after defence** stat. 

Combat begins with the first unit of each army (i.e., the unit at the top of the stack or the front of the queue) getting into combat. Combat between two units (say U1 and U2) proceeds as follows:  

- If the speed of unit U1 is greater than that of U2, U1 attacks first and U2 defends. If U2 is still alive after this, then U2 attacks, and U1 defends.

- If the speeds of U1 and U2 are identical, then both attack and defend simultaneously, regardless of whether one would die in combat.   


ENDING COMBAT
- If at the end of combat (after attack and defence has happened) both units are still alive, they both lose one life. Else, if only one unit remains alive it gains 1 Exp. 

- Alive units return to the army of the player they belong to.  

- Combat is then restarted 


ENDING THE COMBAT
The game ends when at least one army is empty



