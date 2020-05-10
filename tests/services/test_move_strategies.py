import unittest
from data_objects import Rover
from services import move_strategies as ms
from tests.test_environment import rovers
from parameterized import parameterized


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


class TestMoveStrategySelector(unittest.TestCase):

    @parameterized.expand([
        ["north", 'N', 'N'],
        ["east", 'E', 'E'],
        ["west", 'W', 'W'],
        ["south", 'S', 'S']])
    def test_get_strategy_returns_correct_strategy(self, name, cardinal_direction, strategy_cardinal_direction):
        mvs = ms.MoveStrategySelector()
        s = mvs.get_strategy(cardinal_direction)
        self.assertEqual(strategy_cardinal_direction, s.get_cardinal_direction())

    @parameterized.expand([
        ["invalid_cardinal_direction",  '-'],
        ["empty_cardinal_direction",  ''],
        ["None_cardinal_direction",  None]])
    def test_get_strategy_raises_error_for_incorrect_parameters(self, name, cardinal_direction):
        mvs = ms.MoveStrategySelector()
        self.assertRaises(IndexError, mvs.get_strategy, cardinal_direction)
