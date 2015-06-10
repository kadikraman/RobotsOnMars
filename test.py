import unittest
from game import Mars, Robot


class MarsTest(unittest.TestCase):
    def test_constructor(self):
        mars = Mars(3, 4)
        self.assertEqual(mars.max_x, 3)
        self.assertEqual(mars.max_y, 4)
        self.assertEqual(mars.min_x, 0)
        self.assertEqual(mars.min_y, 0)
        self.assertEqual(mars.scented_tiles, [])

    def test_is_location_on_map(self):
        mars = Mars(1, 2)
        self.assertTrue(mars.is_location_on_map(1, 2))
        self.assertTrue(mars.is_location_on_map(0, 0))
        self.assertFalse(mars.is_location_on_map(2, 2))
        self.assertFalse(mars.is_location_on_map(-1, 2))

    def test_add_scented_tile(self):
        mars = Mars(2, 2)
        mars.add_scented_tile(1, 2)
        self.assertTrue([1, 2] in mars.scented_tiles)

    def test_is_tile_scented(self):
        mars = Mars(2, 3)
        mars.add_scented_tile(1, 0)
        self.assertTrue(mars.is_tile_scented(1, 0))


class RobotTest(unittest.TestCase):
    def test_constructor(self):
        robot = Robot(1, 2, 'W', 'FFFFL')
        self.assertEqual(robot.current_x, 1)
        self.assertEqual(robot.current_y, 2)
        self.assertEqual(robot.current_direction, 'W')
        self.assertEqual(robot.instructions, 'FFFFL')
        self.assertFalse(robot.has_been_lost)

    def test_move_forward(self):
        robot = Robot(1, 2, 'N', 'FFF')
        robot.move_forward()
        self.assertEqual(robot.current_x, 1)
        self.assertEqual(robot.current_y, 3)

        robot = Robot(1, 2, 'S', 'FFF')
        robot.move_forward()
        self.assertEqual(robot.current_x, 1)
        self.assertEqual(robot.current_y, 1)

        robot = Robot(1, 2, 'E', 'FFF')
        robot.move_forward()
        self.assertEqual(robot.current_x, 2)
        self.assertEqual(robot.current_y, 2)

        robot = Robot(1, 2, 'W', 'FFF')
        robot.move_forward()
        self.assertEqual(robot.current_x, 0)
        self.assertEqual(robot.current_y, 2)

    def test_move_backward(self):
        robot = Robot(1, 3, 'N', 'FFF')
        robot.move_backward()
        self.assertEqual(robot.current_x, 1)
        self.assertEqual(robot.current_y, 2)

        robot = Robot(1, 1, 'S', 'FFF')
        robot.move_backward()
        self.assertEqual(robot.current_x, 1)
        self.assertEqual(robot.current_y, 2)

        robot = Robot(2, 2, 'E', 'FFF')
        robot.move_backward()
        self.assertEqual(robot.current_x, 1)
        self.assertEqual(robot.current_y, 2)

        robot = Robot(0, 2, 'W', 'FFF')
        robot.move_backward()
        self.assertEqual(robot.current_x, 1)
        self.assertEqual(robot.current_y, 2)

    def test_turn_left(self):
        robot = Robot(1, 2, 'N', 'EFFF')
        self.assertEqual(robot.turn('L'), 'W')

        robot = Robot(1, 2, 'S', 'EFFF')
        self.assertEqual(robot.turn('L'), 'E')

        robot = Robot(1, 2, 'E', 'EFFF')
        self.assertEqual(robot.turn('L'), 'N')

        robot = Robot(1, 2, 'W', 'EFFF')
        self.assertEqual(robot.turn('L'), 'S')
