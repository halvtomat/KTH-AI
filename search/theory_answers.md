# Theory answers 

## Q1
* Possible states consists of all possible subsets of players positions, players scores, fish positions, fish score, time limit. 
* Initial state consists of fish scores and postions for fishes and players and time limit.
* Transition function is dependent on the movement of the players.

## Q2
Terminal states are either when there are no fish left or when the time runs out.

## Q3
It is a good heuristic because it is simple yet it judges a move based on the most important aspect of the game, the score, which is what makes a player win.
The heuristic doesn't use the opponents moves to calculate utility, but in this game the opponent doesn't affect the player that much so it's OK.

## Q4
When a fish is on the hook *v* would probably approximate the utility function pretty good, because then it will find a set of moves that grants an incresed score.

## Q5
If both the red boat and green boat are one move from capturing a fish, but the red boat will capture a bigger (higher score) fish, the heuristic will not consider the fact that the red boat will gain score and will therefore think that the green boat will win that turn.

## Q6
