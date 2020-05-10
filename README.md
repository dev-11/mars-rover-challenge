# Mars Rover Challenge

[![Build Status](https://travis-ci.org/dev-11/mars-rover-challenge.svg?branch=master)](https://travis-ci.org/dev-11/mars-rover-challenge)
[![codecov](https://codecov.io/gh/dev-11/mars-rover-challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/dev-11/mars-rover-challenge)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/76f03ad42cd84729850139f19201e9a2)](https://www.codacy.com/manual/dev-11/mars-rover-challenge?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-11/mars-rover-challenge&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/76f03ad42cd84729850139f19201e9a2)](https://www.codacy.com/manual/dev-11/mars-rover-challenge?utm_source=github.com&utm_medium=referral&utm_content=dev-11/mars-rover-challenge&utm_campaign=Badge_Coverage)

## The approach
I assumed that the incoming commands are stored in a txt file.

The flow of the code is the following:
```text
+----------------------+   +----------------------+   +----------------------+   +----------------------+                
|                      |   |                      |   |                      |   |                      |                
|  reading input data  |-->|   parsing commands   |-->| running rover runner |-->| displaying positions |                
|                      |   |                      |   |                      |   |                      |                
+----------------------+   +----------------------+   +----------------------+   +----------------------+ 
```

### Reading input data
The `repositories.TxtRepository` reads up the given txt file.

### Parsing commands
The `parsers.parse` command expect an array of strings and returns a `Mars` object.
This is the return value of the sample input:
```python
Mars(grid=Grid(max_x=5, max_y=5),
     rover_setups=[
        RoverSetup(rover=Rover(x=1, y=2, cardinal_direction='N'),
                   commands=['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M']),
        RoverSetup(rover=Rover(x=3, y=3, cardinal_direction='E'),
                   commands=['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M'])
    ])
```

### Running rover runner
The `services.RoverRunnerService` executes the commands on the rover inside grid.
To do that the instance of the service needs a `Grid`, a `Rover`, a `MoveStrategySelector`, and a `TurnStrategySelector`.
After the service has been created we need to run the `run` command passing in the commands for the rover.

The  `MoveStrategySelector` and `TurnStrategySelector` return a strategy, based on the actual command.
Here I introduced the [strategy pattern](https://en.wikipedia.org/wiki/Strategy_pattern) to make the life easier, and the code cleaner.

When the runner tries to move the rover off grid the runner will raise a `ValueError`.  

### Displaying positions

The `app.py` acts as a controller, pulls the data and logic together and as the very last step prints out the final position of each rover.

### Tests
I believe I've covered every edge case of the system with my 85 tests.

### Improvements 
At the moment I see two things.

1.  There is no data validation at all, the system assumes that it will receive correct data.
2.  If there is an error, like an invalid command or the rover is going off the grid, the system will fail. It would be nice to have a fail-safe solution where we log and ignore the error and continue the execution of the rover commands.    

### How to run
There is just one dependency which is the [parameterized](https://pypi.org/project/parameterized/) package for the unit tests.

The app can be run by executing the following command. 
```shell script
  app.py -i <input_file>
```

If the app is not given an input file by the `-i` parameter it will reach for the default file.

The unit tests can be run by the following command:
```shell script
  pytest
```

---

## Introduction
Below is a fun coding task that we would like you to complete. It should be considered an opportunity to demonstrate your creativity and ability to think outside the box. The problem demonstrates the minimum required for the output.

You may also include a brief explanation of your design and assumptions along with your code.

## Problem - Mars Rover
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position and location are represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

Write a simple application that takes a user’s starting point, and then directional instructions and displays the resulting position to the user.

### INPUT
The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
 
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.
 
The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.
 
Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

### OUTPUT
The output for each rover should be its final co-ordinates and heading.

#### INPUT AND OUTPUT
Test Input:
```text
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
```
Expected Output:
```text
1 3 N
5 1 E
```
