import unittest
from data_objects import Rover
from services import turn_strategies as ts
from tests.test_environment import rovers
from parameterized import parameterized


class TestTurnLeftFromNorthStrategy(unittest.TestCase):
    def test_turn_turns_rover_to_west(self):
        s = ts.TurnLeftFromNorthStrategy()
        r = s.update(rovers.rover_00N)
        self.assertEqual(Rover(0, 0, 'W'), r)

    def test_turning_direction_is_left(self):
        s = ts.TurnLeftFromNorthStrategy()
        d = s.get_turning_direction()
        self.assertEqual('L', d)

    def test_cardinal_direction_is_north(self):
        s = ts.TurnLeftFromNorthStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('N', d)


class TestTurnLeftFromWestStrategy(unittest.TestCase):
    def test_turn_turns_rover_to_south(self):
        s = ts.TurnLeftFromWestStrategy()
        r = s.update(rovers.rover_00W)
        self.assertEqual(Rover(0, 0, 'S'), r)

    def test_turning_direction_is_left(self):
        s = ts.TurnLeftFromWestStrategy()
        d = s.get_turning_direction()
        self.assertEqual('L', d)

    def test_cardinal_direction_is_west(self):
        s = ts.TurnLeftFromWestStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('W', d)


class TestTurnLeftFromEastStrategy(unittest.TestCase):
    def test_turn_turns_rover_to_north(self):
        s = ts.TurnLeftFromEastStrategy()
        r = s.update(rovers.rover_00E)
        self.assertEqual(Rover(0, 0, 'N'), r)

    def test_turning_direction_is_left(self):
        s = ts.TurnLeftFromEastStrategy()
        d = s.get_turning_direction()
        self.assertEqual('L', d)

    def test_cardinal_direction_is_east(self):
        s = ts.TurnLeftFromEastStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('E', d)


class TestTurnLeftFromSouthStrategy(unittest.TestCase):
    def test_turn_turns_rover_to_east(self):
        s = ts.TurnLeftFromSouthStrategy()
        r = s.update(rovers.rover_00S)
        self.assertEqual(Rover(0, 0, 'E'), r)

    def test_turning_direction_is_left(self):
        s = ts.TurnLeftFromSouthStrategy()
        d = s.get_turning_direction()
        self.assertEqual('L', d)

    def test_cardinal_direction_is_south(self):
        s = ts.TurnLeftFromSouthStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('S', d)


class TestTurnRightFromNorthStrategy(unittest.TestCase):
    def test_turn_turns_rover_to_east(self):
        s = ts.TurnRightFromNorthStrategy()
        r = s.update(rovers.rover_00N)
        self.assertEqual(Rover(0, 0, 'E'), r)

    def test_turning_direction_is_left(self):
        s = ts.TurnRightFromNorthStrategy()
        d = s.get_turning_direction()
        self.assertEqual('R', d)

    def test_cardinal_direction_is_north(self):
        s = ts.TurnRightFromNorthStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('N', d)


class TestTurnRightFromWestStrategy(unittest.TestCase):
    def test_turn_turns_rover_to_north(self):
        s = ts.TurnRightFromWestStrategy()
        r = s.update(rovers.rover_00W)
        self.assertEqual(Rover(0, 0, 'N'), r)

    def test_turning_direction_is_left(self):
        s = ts.TurnRightFromWestStrategy()
        d = s.get_turning_direction()
        self.assertEqual('R', d)

    def test_cardinal_direction_is_west(self):
        s = ts.TurnRightFromWestStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('W', d)


class TestTurnRightFromEastStrategy(unittest.TestCase):
    def test_turn_turns_rover_to_south(self):
        s = ts.TurnRightFromEastStrategy()
        r = s.update(rovers.rover_00E)
        self.assertEqual(Rover(0, 0, 'S'), r)

    def test_turning_direction_is_left(self):
        s = ts.TurnRightFromEastStrategy()
        d = s.get_turning_direction()
        self.assertEqual('R', d)

    def test_cardinal_direction_is_east(self):
        s = ts.TurnRightFromEastStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('E', d)


class TestTurnRightFromSouthStrategy(unittest.TestCase):
    def test_turn_turns_rover_to_west(self):
        s = ts.TurnRightFromSouthStrategy()
        r = s.update(rovers.rover_00S)
        self.assertEqual(Rover(0, 0, 'W'), r)

    def test_turning_direction_is_left(self):
        s = ts.TurnRightFromSouthStrategy()
        d = s.get_turning_direction()
        self.assertEqual('R', d)

    def test_cardinal_direction_is_south(self):
        s = ts.TurnRightFromSouthStrategy()
        d = s.get_cardinal_direction()
        self.assertEqual('S', d)


class TestStrategyCollection(unittest.TestCase):
    def test_get_turn_strategies_return_every_item(self):
        lst = ts.get_turn_strategies()
        self.assertEqual(8, len(lst))


class TestMoveStrategySelector(unittest.TestCase):

    @parameterized.expand([
        ["left_north",  'N', 'N', 'L', 'L'],
        ["left_east",   'E', 'E', 'L', 'L'],
        ["left_west",   'W', 'W', 'L', 'L'],
        ["left_south",  'S', 'S', 'L', 'L'],
        ["right_north", 'N', 'N', 'R', 'R'],
        ["right_east",  'E', 'E', 'R', 'R'],
        ["right_west",  'W', 'W', 'R', 'R'],
        ["right_south", 'S', 'S', 'R', 'R']])
    def test_get_strategy_returns_correct_strategy(self, name, cardinal_direction, strategy_cardinal_direction,
                                                   turning_direction, strategy_turning_direction):
        mvs = ts.TurnStrategySelector()
        s = mvs.get_strategy(cardinal_direction, turning_direction)
        self.assertEqual(strategy_cardinal_direction, s.get_cardinal_direction())
        self.assertEqual(strategy_turning_direction, s.get_turning_direction())

    @parameterized.expand([
        ["invalid_cardinal_direction",  '-', 'L'],
        ["empty_cardinal_direction", '', 'L'],
        ["invalid_turning_direction",  'N', '-'],
        ["empty_turning_direction", 'N', ''],
        ["None_cardinal_direction", None, 'L'],
        ["None_turning_direction", 'N', None],
        ["both_params_None", None, None],
        ["both_params_empty", '', ''],
        ["both_params_invalid",  '-', '-']])
    def test_get_strategy_raises_error_for_incorrect_parameters(self, name, cardinal_direction, turning_direction):
        mvs = ts.TurnStrategySelector()
        self.assertRaises(IndexError, mvs.get_strategy, cardinal_direction, turning_direction)
