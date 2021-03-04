# Theory answers 

## Q1
* Possible states consists of all possible of players positions, players scores, fish positions. 
* Initial state consists of fish scores and postions for fishes and players and time limit.
* Transition function is dependent on the chosen action of the player.

## Q2
Terminal states are either when there are no fish left or when the time runs out.

## Q3
It is a good heuristic because it is simple yet it judges a move based on the most important aspect of the game, the score, which is what makes a player win. It's also good that the heuristic takes into account the score of the red boat so that the mini part of the minimax function can predict the moves of the red boat.

## Q4
When a fish is on the hook *v* would probably approximate the utility function pretty good, because then it will find a set of moves that grants an incresed score.

## Q5
If both the red boat and green boat are one move from capturing a fish, but the red boat will capture a bigger (higher score) fish, the heuristic will not consider the fact that the red boat will gain score and will therefore think that the green boat will win that turn.

## Q6
It will not have the same problem as the previous one, however it will have another problem that is in some games (like chess), it will be very hard to find all terminal states because of the depth needed to reach them.