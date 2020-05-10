import unittest
from data_objects import Rover
from services import move_commands as mc
from tests.test_environment import rovers
from parameterized import parameterized


class TestMoveToNorthCommand(unittest.TestCase):
    def test_move_moves_rover_to_north(self):
        s = mc.MoveToNorthCommand()
        r = s.execute(rovers.rover_00N)
        self.assertEqual(Rover(0, 1, 'N'), r)

    def test_cardinal_direction_is_north(self):
        s = mc.MoveToNorthCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('N', d)


class TestMoveToEastCommand(unittest.TestCase):
    def test_move_moves_rover_to_east(self):
        s = mc.MoveToEastCommand()
        r = s.execute(rovers.rover_00E)
        self.assertEqual(Rover(1, 0, 'E'), r)

    def test_cardinal_direction_is_east(self):
        s = mc.MoveToEastCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('E', d)


class TestMoveToWestCommand(unittest.TestCase):
    def test_move_moves_rover_to_west(self):
        s = mc.MoveToWestCommand()
        r = s.execute(rovers.rover_00W)
        self.assertEqual(Rover(-1, 0, 'W'), r)

    def test_cardinal_direction_is_west(self):
        s = mc.MoveToWestCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('W', d)


class TestMoveToSouthCommand(unittest.TestCase):
    def test_move_moves_rover_to_south(self):
        s = mc.MoveToSouthCommand()
        r = s.execute(rovers.rover_00S)
        self.assertEqual(Rover(0, -1, 'S'), r)

    def test_cardinal_direction_is_south(self):
        s = mc.MoveToSouthCommand()
        d = s.get_cardinal_direction()
        self.assertEqual('S', d)


class TestCommandCollection(unittest.TestCase):
    def test_get_move_commands_return_every_item(self):
        lst = mc.get_move_commands()
        self.assertEqual(4, len(lst))


class TestMoveCommandSelector(unittest.TestCase):

    @parameterized.expand([
        ["north", 'N', 'N'],
        ["east", 'E', 'E'],
        ["west", 'W', 'W'],
        ["south", 'S', 'S']])
    def test_get_command_returns_correct_Command(self, name, cardinal_direction, Command_cardinal_direction):
        mvs = mc.MoveCommandSelector()
        s = mvs.get_command(cardinal_direction)
        self.assertEqual(Command_cardinal_direction, s.get_cardinal_direction())

    @parameterized.expand([
        ["invalid_cardinal_direction",  '-'],
        ["empty_cardinal_direction",  ''],
        ["None_cardinal_direction",  None]])
    def test_get_command_raises_error_for_incorrect_parameters(self, name, cardinal_direction):
        mvs = mc.MoveCommandSelector()
        self.assertRaises(IndexError, mvs.get_command, cardinal_direction)
