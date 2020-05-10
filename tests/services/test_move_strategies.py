import unittest
from data_objects import Rover
from services import move_strategies as ms
from tests.test_environment import rovers


class TestMoveToNorthStrategy(unittest.TestCase):
    def test_move_moves_rover_to_north(self):
        s = ms.MoveToNorthStrategy()
        r = s.update(rovers.rover_00N)
        self.assertEqual(Rover(0, 1, 'N'), r)

    def test_cardinal_direction_is_north(self):
        s = ms.MoveToNorthStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('N', d)


class TestMoveToEastStrategy(unittest.TestCase):
    def test_move_moves_rover_to_east(self):
        s = ms.MoveToEastStrategy()
        r = s.update(rovers.rover_00E)
        self.assertEqual(Rover(1, 0, 'E'), r)

    def test_cardinal_direction_is_east(self):
        s = ms.MoveToEastStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('E', d)


class TestMoveToWestStrategy(unittest.TestCase):
    def test_move_moves_rover_to_west(self):
        s = ms.MoveToWestStrategy()
        r = s.update(rovers.rover_00W)
        self.assertEqual(Rover(-1, 0, 'W'), r)

    def test_cardinal_direction_is_west(self):
        s = ms.MoveToWestStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('W', d)


class TestMoveToSouthStrategy(unittest.TestCase):
    def test_move_moves_rover_to_south(self):
        s = ms.MoveToSouthStrategy()
        r = s.update(rovers.rover_00S)
        self.assertEqual(Rover(0, -1, 'S'), r)

    def test_cardinal_direction_is_south(self):
        s = ms.MoveToSouthStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('S', d)


class TestStrategyCollection(unittest.TestCase):
    def test_get_move_strategies_return_every_item(self):
        lst = ms.get_move_strategies()
        self.assertEqual(4, len(lst))
