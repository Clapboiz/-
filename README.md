# Scientific research

## About web pentest
**Define reward:**

  * Gather new information
    
    * Learning about new marchine: 5 reward
    * Checking an exploit and learning it is valuable: 1 reward
    * Garthering loot provides 1 reward, 5 reward for password hashes
    
    **_=> This is only for new information and Garthering loot mean "loot" is valuable documents or information that an attacker can obtain from a compromised system_**

  * Successfully excuting vulnerablities:
    * Give 10 reward
    * Gaining superuser privileges (Admintrator): 20 reward

  * Movement fails: -1 reward

## Custom env
**_FlatActionSpace:_**

**Meaning in Pentest Context:**
 
  **Each action is a specific task that a learning agent can perform.**
 
  _For example:_
   
   * Action 1: "Exploit Vulnerability A"
   * Action 2: "Scan service B"
   * Action 3: "Elevate privileges"
   * Each action corresponds to a specific job that the agent can choose.

**_ParameterizedActionSpace:_**

**Meaning in Pentest Context:**

**Each action can be performed with different parameters, creating multiple variations of an action type.**

_For example:_

   * Action: "Exploit Vulnerability"
   * Parameter 1: Vulnerability type (A, B, C)
   * Parameter 2: Target (Server 1, Server 2)
   * Parameter 3: Privilege level (User, Root)
    
In this way, the agent can perform the "Vulnerability Exploitation" action with many different variations by changing the parameters.

**Why are there only 2 Action Spaces:**

**_Provide these two action spaces to accommodate the diversity of tasks and learning requirements. Flexibility helps the learning agent model learn how to interact with the environment and perform takedown testing tasks effectively._**

## References
[1] _"Training an Autonomous Pentester with Deep RL" by Shane Caldwell. Link: "https://www.thestrangeloop.com/2021/training-an-autonomous-pentester-with-deep-rl.html"_

...
