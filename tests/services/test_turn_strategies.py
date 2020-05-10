import unittest
from data_objects import Rover
from services import turn_strategies as ts
from tests.test_environment import rovers


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
