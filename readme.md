# Robots on Mars

[![Code Climate](https://codeclimate.com/github/kadikraman/RobotsOnMars/badges/gpa.svg)](https://codeclimate.com/github/kadikraman/RobotsOnMars)
[![Build Status](https://travis-ci.org/kadikraman/RobotsOnMars.svg?branch=master)](https://travis-ci.org/kadikraman/RobotsOnMars)

A little game featuring some robots traversing the surface of Mars.

## Running the app
- must have **Python 2.7 or higher** installed
- add/edit the instructions for the robots and the map in **instructions.txt**
- execute the following command in the project root directory:
```
python main.py
```

## Running the tests
Execute the following command in the project root directory
```
python -m unittest discover .
```

## Input
- The first line of input is the upper-right coordinates of the rectangular world, the lower-left coordinates are assumed to be 0, 0.
- The remaining input consists of a sequence of robot positions and instructions (two lines per robot).
A position consists of two integers specifying the initial coordinates of the robot and an orientation (N, S, E, W), all
separated by whitespace on one line. A robot instruction is a string of the letters “L”, “R”, and “F” on one line.

## Output
For each robot position/instruction in the input, the output should indicate the final grid position and orientation of the robot.
If a robot falls off the edge of the grid the word “LOST” should be printed after the position and orientation.


## Things to be aware of
- Other than checking whether the instructions file exists, there is *no* error handling or input sanitizing. None. So if you input 'potato', you will receive an exception.
- When a robot 'falls off the edge', it continues 'moving'. So technically the same robot could fall of the edge twice (and thus leave two 'scents').
