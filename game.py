"""
Holds the Robot and Mars Map classes
"""

class Robot:
    """
    Contains the robot game element. Knows its current position and how to move based on letter instructions
    """
    def __init__(self, start_x, start_y, start_direction, instructions):
        self.current_x = start_x
        self.current_y = start_y
        self.current_direction = start_direction
        self.instructions = instructions

    def move_forward(self):
        """
        Moves the robot forward one step
        :return: x, y coordinates of the new position
        """
        if self.current_direction == 'N':
            self.current_y += 1
        elif self.current_direction == 'E':
            self.current_x += 1
        elif self.current_direction == 'S':
            self.current_y -= 1
        elif self.current_direction == 'W':
            self.current_x -= 1
        return self.current_x, self.current_y

    def turn(self, instruction):
        """
        Turns the robot left or right based on the instruction
        :param instruction: 'L' or 'R'
        :return: new direction
        """
        directions = ['N', 'E', 'S', 'W']
        left = ['W', 'N', 'E', 'S']
        right = ['E', 'S', 'W', 'N']
        index = directions.index(self.current_direction)
        if instruction == 'L':
            self.current_direction = left[index]
        elif instruction == 'R':
            self.current_direction = right[index]
        return self.current_direction


class Mars:
    """
    Contains the surface grid of mars and a list of 'scented tiles' (tiles from which robots cannot fall off)
    """
    def __init__(self, max_x, max_y):
        """
        Initialises the mars map.
        :param max_x: maximum top right x-coordinate of the map
        :param max_y: maximum top right y-coordinate of the map
        :return:
        """
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = 0
        self.min_y = 0
        self.scented_tiles = []

    def is_location_on_map(self, x, y):
        """
        Checks if a given (x, y) coordinate is on the map
        :param x: x coordinate
        :param y: y coordinate
        :return: True if the location is on the map, False otherwise
        """
        return self.max_x >= x >= 0 and self.max_y >= y >= 0
