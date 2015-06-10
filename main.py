from game import Mars, Robot


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
    mars = Mars(5, 3)
    robot1 = Robot(1, 1, 'E', 'RFRFRFRF')
    robot2 = Robot(3, 2, 'N', 'FRRFLLFFRRFLL')
    robot3 = Robot(0, 3, 'W', 'LLFFFLFLFL')
    robots = [robot1, robot2, robot3]

    print(play(mars, robots))


if __name__ == '__main__':
    main()