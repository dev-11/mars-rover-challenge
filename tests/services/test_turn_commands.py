import unittest
from data_objects import Rover
from services import turn_commands as tc
from tests.test_environment import rovers
from parameterized import parameterized


class TestTurnLeftFromNorthCommand(unittest.TestCase):
    def test_turn_turns_rover_to_west(self):
        s = tc.TurnLeftFromNorthCommand()
        r = s.execute(rovers.rover_00N)
        self.assertEqual(Rover(0, 0, 'W'), r)

    def test_turning_direction_is_left(self):
        s = tc.TurnLeftFromNorthCommand()
        d = s.get_turning_direction()
        self.assertEqual('L', d)

    def test_cardinal_direction_is_north(self):
        s = tc.TurnLeftFromNorthCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('N', d)


class TestTurnLeftFromWestCommand(unittest.TestCase):
    def test_turn_turns_rover_to_south(self):
        s = tc.TurnLeftFromWestCommand()
        r = s.execute(rovers.rover_00W)
        self.assertEqual(Rover(0, 0, 'S'), r)

    def test_turning_direction_is_left(self):
        s = tc.TurnLeftFromWestCommand()
        d = s.get_turning_direction()
        self.assertEqual('L', d)

    def test_cardinal_direction_is_west(self):
        s = tc.TurnLeftFromWestCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('W', d)


class TestTurnLeftFromEastCommand(unittest.TestCase):
    def test_turn_turns_rover_to_north(self):
        s = tc.TurnLeftFromEastCommand()
        r = s.execute(rovers.rover_00E)
        self.assertEqual(Rover(0, 0, 'N'), r)

    def test_turning_direction_is_left(self):
        s = tc.TurnLeftFromEastCommand()
        d = s.get_turning_direction()
        self.assertEqual('L', d)

    def test_cardinal_direction_is_east(self):
        s = tc.TurnLeftFromEastCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('E', d)


class TestTurnLeftFromSouthCommand(unittest.TestCase):
    def test_turn_turns_rover_to_east(self):
        s = tc.TurnLeftFromSouthCommand()
        r = s.execute(rovers.rover_00S)
        self.assertEqual(Rover(0, 0, 'E'), r)

    def test_turning_direction_is_left(self):
        s = tc.TurnLeftFromSouthCommand()
        d = s.get_turning_direction()
        self.assertEqual('L', d)

    def test_cardinal_direction_is_south(self):
        s = tc.TurnLeftFromSouthCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('S', d)


class TestTurnRightFromNorthCommand(unittest.TestCase):
    def test_turn_turns_rover_to_east(self):
        s = tc.TurnRightFromNorthCommand()
        r = s.execute(rovers.rover_00N)
        self.assertEqual(Rover(0, 0, 'E'), r)

    def test_turning_direction_is_left(self):
        s = tc.TurnRightFromNorthCommand()
        d = s.get_turning_direction()
        self.assertEqual('R', d)

    def test_cardinal_direction_is_north(self):
        s = tc.TurnRightFromNorthCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('N', d)


class TestTurnRightFromWestCommand(unittest.TestCase):
    def test_turn_turns_rover_to_north(self):
        s = tc.TurnRightFromWestCommand()
        r = s.execute(rovers.rover_00W)
        self.assertEqual(Rover(0, 0, 'N'), r)

    def test_turning_direction_is_left(self):
        s = tc.TurnRightFromWestCommand()
        d = s.get_turning_direction()
        self.assertEqual('R', d)

    def test_cardinal_direction_is_west(self):
        s = tc.TurnRightFromWestCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('W', d)


class TestTurnRightFromEastCommand(unittest.TestCase):
    def test_turn_turns_rover_to_south(self):
        s = tc.TurnRightFromEastCommand()
        r = s.execute(rovers.rover_00E)
        self.assertEqual(Rover(0, 0, 'S'), r)

    def test_turning_direction_is_left(self):
        s = tc.TurnRightFromEastCommand()
        d = s.get_turning_direction()
        self.assertEqual('R', d)

    def test_cardinal_direction_is_east(self):
        s = tc.TurnRightFromEastCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('E', d)


class TestTurnRightFromSouthCommand(unittest.TestCase):
    def test_turn_turns_rover_to_west(self):
        s = tc.TurnRightFromSouthCommand()
        r = s.execute(rovers.rover_00S)
        self.assertEqual(Rover(0, 0, 'W'), r)

    def test_turning_direction_is_left(self):
        s = tc.TurnRightFromSouthCommand()
        d = s.get_turning_direction()
        self.assertEqual('R', d)

    def test_cardinal_direction_is_south(self):
        s = tc.TurnRightFromSouthCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('S', d)


class TestCommandCollection(unittest.TestCase):
    def test_get_turn_commands_return_every_item(self):
        lst = tc.get_turn_commands()
        self.assertEqual(8, len(lst))


class TestMoveCommandSelector(unittest.TestCase):

    @parameterized.expand([
        ["left_north",  'N', 'N', 'L', 'L'],
        ["left_east",   'E', 'E', 'L', 'L'],
        ["left_west",   'W', 'W', 'L', 'L'],
        ["left_south",  'S', 'S', 'L', 'L'],
        ["right_north", 'N', 'N', 'R', 'R'],
        ["right_east",  'E', 'E', 'R', 'R'],
        ["right_west",  'W', 'W', 'R', 'R'],
        ["right_south", 'S', 'S', 'R', 'R']])
    def test_get_command_returns_correct_command(self, name, cardinal_direction, command_cardinal_direction,
                                                   turning_direction, command_turning_direction):
        mvs = tc.TurnCommandSelector()
        s = mvs.get_command(cardinal_direction, turning_direction)
        self.assertEqual(command_cardinal_direction, s.get_cardinal_direction())
        self.assertEqual(command_turning_direction, s.get_turning_direction())

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
    def test_get_command_raises_error_for_incorrect_parameters(self, name, cardinal_direction, turning_direction):
        mvs = tc.TurnCommandSelector()
        self.assertRaises(IndexError, mvs.get_command, cardinal_direction, turning_direction)
