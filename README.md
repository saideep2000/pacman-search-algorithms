# Pacman Simulation

This is Programming Assignment 1 in the Foundation of Artificial Intelligence

This is used from Berkeley Pacman project.
https://inst.eecs.berkeley.edu/~cs188/fa22/projects/proj1/

To download initial code:
https://inst.eecs.berkeley.edu/~cs188/fa22/assets/projects/search.zip

## Project

In the project, we have:

### `Features`

1. Depth First Search (DFS):

Implement the DFS algorithm to find a path through Pacman's maze.
It needs to return a list of actions leading from the start to the goal.
Should not move through walls or perform illegal moves.

2. Breadth First Search (BFS):

Implement BFS to find the shortest path in Pacman's world.
It should not expand states that have been previously visited.

3. Uniform-Cost Search:

Adjust the cost function to get Pacman to follow different paths. The goal is to find the least-cost solution.
Charge differently for different paths such as those with ghosts or food-rich areas.

4. A Search*:

Implement the A* algorithm which uses a heuristic function to help guide the search.
The Manhattan distance heuristic is provided, but you might need to use other heuristics or implement your own.

5. Finding All the Corners:

Develop an algorithm where Pacman needs to touch all four corners of the maze.
Implement the CornersProblem search problem to handle this situation.
Make sure to use an abstract state representation that is efficient.

6. Corners Problem: Heuristic:

Implement a consistent heuristic for the CornersProblem to optimize the A* search.
The heuristic must be non-trivial and consistent to get full credit.

7. Eating All The Dots:

Solve the problem of Pacman eating all the food in the least number of steps.
This uses the FoodSearchProblem.
Implement a consistent heuristic for this problem to make A* search more efficient.

**Note: This is just a code uploaded for reference and as a `practice`, towards AI!**

## Process of project done

### Instructions:
This has 8 parts:

Q1 (3 pts): Finding a Fixed Food Dot using Depth First Search

Q2 (3 pts): Breadth First Search

Q3 (3 pts): Varying the Cost Function

Q4 (3 pts): A* search

Q5 (3 pts): Finding All the Corners

Q6 (3 pts): Corners Problem: Heuristic

Q7 (4 pts): Eating All The Dots

Q8 (3 pts): Suboptimal Search

#### Autograder is available for correctness of the code.

#### Files you'll edit:

search.py 	Where all of your search algorithms will reside.

searchAgents.py 	Where all of your search-based agents will reside.

#### Files you might want to look at:
pacman.py 	The main file that runs Pacman games. This file describes a Pacman GameState type, which you use in this project.

game.py 	The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid.

util.py 	Useful data structures for implementing search algorithms.

#### Ignore Other Files

#### Submission:
token generated by submission_autograder.py

### Things Used:

### Shortcuts that help (mac):
python version - python3

python3 pacman.py

#### Agents:
python3 pacman.py --layout testMaze --pacman GoWestAgent

python3 pacman.py --layout tinyMaze --pacman GoWestAgent

CTRL + C in terminal to exit the game.

##### For list of options:
python3 pacman.py -h

python3 pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

##### Commnads Useful for Questions:

###### Q1 (DFS):
python3 pacman.py -l tinyMaze -p SearchAgent
python3 pacman.py -l mediumMaze -p SearchAgent
python3 pacman.py -l bigMaze -z .5 -p SearchAgent

python3 autograder.py -q q1

printing states : print(list(stack.list))

###### Q2 (BFS):

python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

python3 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

python3 autograder.py -q q2

###### Q3 (UCS):

python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

python3 pacman.py -l mediumDottedMaze -p StayEastSearchAgent

python3 pacman.py -l mediumScaryMaze -p StayWestSearchAgent


python3 autograder.py -q q3

###### Q4 (AStar):

python3 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

python3 autograder.py -q q4

###### Q5 (Finding all the Corners):

python3 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python3 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

python3 autograder.py -q q5
    
###### Q6 (Corners Problem Heuristic):

python3 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

-p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic

python3 autograder.py -q q6

###### Q7 (Eating all the dots):

python3 pacman.py -l testSearch -p AStarFoodSearchAgent

-p SearchAgent -a fn=astar,prob=FoodSearchProblem,heuristic=foodHeuristic

python3 pacman.py -l trickySearch -p AStarFoodSearchAgent

python3 autograder.py -q q7


###### Q8 (Suboptimal Search):

python3 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5

python3 autograder.py -q q8


###### Token generated:

python submission_autograder.py



## Happy Coding...
