import unittest
from data_objects import Rover
from services import move_strategies as ms
from tests.test_environment import rovers


class TestMoveToNorthStrategy(unittest.TestCase):
    def test_move_moves_rover_to_north(self):
        s = ms.MoveToNorthStrategy()
        r = s.update(rovers.rover_00N)
        self.assertEqual(Rover(0, 1, 'N'), r)


class TestMoveToEastStrategy(unittest.TestCase):
    def test_move_moves_rover_to_east(self):
        s = ms.MoveToEastStrategy()
        r = s.update(rovers.rover_00E)
        self.assertEqual(Rover(1, 0, 'E'), r)


class TestMoveToWestStrategy(unittest.TestCase):
    def test_move_moves_rover_to_west(self):
        s = ms.MoveToWestStrategy()
        r = s.update(rovers.rover_00W)
        self.assertEqual(Rover(-1, 0, 'W'), r)


class TestMoveToSouthStrategy(unittest.TestCase):
    def test_move_moves_rover_to_south(self):
        s = ms.MoveToSouthStrategy()
        r = s.update(rovers.rover_00S)
        self.assertEqual(Rover(0, -1, 'S'), r)
