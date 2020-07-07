# Teaching Pac-Man to Search for food

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
    