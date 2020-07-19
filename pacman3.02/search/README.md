# Teaching Pac-Man to Search for food

```
This lab is possible thanks to the generous contributions of the UC Berkeley AI division and their work on the Pac-Man Project.
http://ai.berkeley.edu/search.html
```

Teach Pac-Man to search his world to complete the following tasks:
- find a single obstacle.
- find multiple obstacles.
- find the fastest way to eat all the food in the map.

![](pacman.gif)


# Program Pacman agent to find paths through its maze world
- Both to reach a particular location and to collect food efficiently.
- Build general search algorithms and apply them to Pacman scenarios.

## Files to edit:
File | Desc
--- | --- 
search.py             |   Where all search algorithms will reside.
searchAgents.py        |   Where all search-based agents will reside.

## Files to look at:
File | Desc
--- | --- 
pacman.py             |   The main file that runs Pacman games. File describes a Pacman GameState type, to use in this project.
game.py               |   The logic behind how the Pacman world works. This file describes several supporting types like AgentState, Agent, Direction, and Grid.
util.py               |   Useful data structures for implementing search algorithms.

## Supporting files:
File | Desc
--- | --- 
graphicsDisplay.py    |   Graphics for Pacman
graphicsUtils.py      |   Support for Pacman graphics
textDisplay.py        |   ASCII graphics for Pacman
ghostAgents.py        |   Agents to control ghosts
keyboardAgents.py     |   Keyboard interfaces to control Pacman
layout.py             |   Code for reading layout files and storing their contents
autograder.py         |   Project autograder
testParser.py         |   Parses autograder test and solution files
testClasses.py        |   General autograding test classes
test_cases/           |   Directory containing the test cases for each question
searchTestClasses.py   |   Project specific autograding test classes

# How to play

```python pacman.py
    - Pacman lives in a shiny blue world of twisting corridors and tasty round treats. 
    - Navigating this world efficiently will be Pacman first step in mastering his domain.
    - python pacman.py -h to see the list of all options and their default values.
    - if Pacman gets stuck, exit the game by typing CTRL-c into your terminal.
```

###     - The simplest agent in searchAgents.py is called the GoWestAgent, which always goes West (a trivial reflex agent). This agent can occasionally win:

```
python pacman.py --layout testMaze --pacman GoWestAgent
```

###     - But, things get ugly for this agent when turning is required:

```
python pacman.py --layout tinyMaze --pacman GoWestAgent
```

Soon, agent will solve not only tinyMaze, but any maze we want :)

### Note 
    - pacman.py supports a number of options that can each be expressed in a long way (e.g., --layout) or a short way (e.g., -l).
    - See the list of all options and their default values via: python pacman.py -h

    - Also, all of the commands that appear in this project also appear in commands.txt, for easy copying and pasting. 
    - In UNIX/Mac OS X, you can even run all these commands in order with bash commands.txt.

# Program 1: Finding a Fixed Food Dot using Depth First Search

## In searchAgents.py, you'll find a fully implemented SearchAgent, 
- which plans out a path through Pacman's world and then 
- executes that path step-by-step.

## The search algorithms for formulating a plan are not implemented -- that's your job.
### - As you work through the following questions, you might find it useful to refer to the object glossary 
### - (the second to last tab in the navigation bar above).

## First, test that the SearchAgent is working correctly by running:

```
python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
```

- The command above tells the SearchAgent to use tinyMazeSearch as its search algorithm, which is implemented in search.py. 
- Pacman should navigate the maze successfully.

## Write full-fledged generic search functions to help Pacman plan routes.
- Remember that a search node must contain not only a state but also the information necessary to reconstruct the plan which gets to that state.
- Important note: All of your search functions need to return a list of actions that will lead the agent from the start to the goal.
- These actions all have to be legal moves (valid directions, no moving through walls).

### Important note
- Make sure to use the Stack, Queue and PriorityQueue data structures provided to you in util.py
- These data structure implementations have particular properties which are required for compatibility with the autograder.

### Hint: 
- Each algorithm is very similar. 
- Algorithms for DFS, BFS, UCS, and A* differ only in the details of how the fringe is managed.
- So, concentrate on getting DFS right and the rest should be relatively straightforward. 
- Indeed, one possible implementation requires only a single generic search method which is configured with an algorithm-specific queuing strategy.
- (Your implementation need not be of this form to receive full credit).

### Implement the depth-first search (DFS) algorithm in the depthFirstSearch function in search.py.
- To make your algorithm complete, write the graph search version of DFS, which avoids expanding any already visited states.

### Your code should quickly find a solution for:
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```

### The Pacman board will show an overlay of the states explored, and the order in which they were explored (brighter red means earlier exploration).
- Is the exploration order what you would have expected? 
- Does Pacman actually go to all the explored squares on his way to the goal?

### Hint: 
- If you use a Stack as your data structure, the solution found by DFS algorithm for mediumMaze should have a length of 130 
    - (provided you push successors onto the fringe in the order provided by getSuccessors; you might get 246 if you push them in the reverse order). 
- Is this a least cost solution? 
    - If not, think about what depth-first search is doing wrong.

# Program 2: Breadth First Search

Implement the breadth-first search (BFS) algorithm in the breadthFirstSearch function in search.py. 
Write a graph search algorithm that avoids expanding any already visited states.
Test your code the same way you did for depth-first search.

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

Does BFS find a least cost solution? If not, check your implementation.

Hint: If Pacman moves too slowly for you, try the option --frameTime 0.

Note: If you've written your search code generically, your code should work equally well for the eight-puzzle search problem without any changes.

python eightpuzzle.py


# Program 3: Varying the Cost Function

- BFS finds a fewest-actions path to the goal
- Here we might want to find paths that are "best" in other senses. 

Consider mediumDottedMaze and mediumScaryMaze.
- By changing cost function, we can encourage Pacman to find different paths. 
- For example, we can charge more for dangerous steps in ghost-ridden areas or less for steps in food-rich areas, and a rational Pacman agent should adjust its behavior in response.

Implement uniform-cost graph search algorithm in the uniformCostSearch function in search.py. 
- We encourage you to look through util.py for some data structures that may be useful in your implementation. 
- You should now observe successful behavior in all three of the following layouts, where the agents below are all UCS agents that differ only in the cost function they use

```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

## Note: 
- You should get very low and very high path costs for the StayEastSearchAgent and StayWestSearchAgent respectively, 
- -  due to their exponential cost functions (see searchAgents.py for details).