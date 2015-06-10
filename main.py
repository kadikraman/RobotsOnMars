from game import Mars, Robot
import sys


def read_instructions(filename):
    """
    Reads the data from file, parses it and turns it into Robot/Mars objects
    :param filename: name of the file to read from
    :return: Mars map object and Robot array
    """

    # reads the raw data from file
    try:
        with open(filename) as f:
            instructions = f.read().splitlines()
    except IOError:
        sys.exit('IOError: Instructions not where expected! Please create an instructions.txt file')

    # first line should be the map coordinates
    map_coordinates = instructions[0].split(' ')
    mars = Mars(int(map_coordinates[0]), int(map_coordinates[1]))

    # the robot data are two lines each with a blank line in between
    robot_data = []
    for line in range(0, len(instructions), 3):
        robot_data.append([instructions[line+1], instructions[line+2]])

    # create the robots
    robots = []
    for data in robot_data:
        # first line is initial position and direction
        initial_position = data[0].split(' ')
        x = int(initial_position[0])
        y = int(initial_position[1])
        position = initial_position[2]
        # second line is the instruction string
        instructions = data[1]
        robots.append(Robot(x, y, position, instructions))

    return mars, robots



def generate_output_string(robots):
    """
    Generate the output string based on current state of the robots
    :param robots: array of Robots
    :return: output string
    """
    output = ''
    for robot in robots:
        output += "{0} {1} {2}{3}\n".format(robot.current_x, robot.current_y, robot.current_direction,
                                            ' LOST' if robot.has_been_lost else '')
    return output


def play(mars, robots):
    """
    Play! The game logic lives here.
    Robots traverse Mars in order. If the fall of the map, the tile they were standing on becomes 'scented'
    so that future robots will not fall off that tile (the instruction will be ignored)
    :param robots: array of Robots
    :param mars: map of Mars
    :return: result string
    """
    for robot in robots:
        for instruction in robot.instructions:
            if instruction in ['L', 'R']:
                robot.turn(instruction)
            elif instruction in ['F']:
                current_x = robot.current_x
                current_y = robot.current_y
                x, y = robot.move_forward()
                if not mars.is_location_on_map(x, y):
                    if not mars.is_tile_scented(current_x, current_y):
                        mars.add_scented_tile(current_x, current_y)
                        robot.has_been_lost = True
                    else:
                        robot.move_backward()
    return generate_output_string(robots)

def main():
    """
    Main entry point of the application
    """
    mars, robots = read_instructions('instructions.txt')
    result = play(mars, robots)
    print result


if __name__ == '__main__':
    main()