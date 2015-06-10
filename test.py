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


class RobotTest(unittest.TestCase):
    def test_constructor(self):
        robot = Robot(1, 2, 'W', 'FFFFL')
        self.assertEqual(robot.current_x, 1)
        self.assertEqual(robot.current_y, 2)
        self.assertEqual(robot.current_position, 'W')
        self.assertEqual(robot.instructions, 'FFFFL')