import unittest
from services import RoverRunnerService
from tests.test_environment.marses import small_mars_with_one_rover_empty_commands
from tests.test_environment import mocks as m
from data_objects import Rover


class TestRoverRunnerService(unittest.TestCase):

    def test_rover_runner_moves_rover_forward(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = small_mars_with_one_rover_empty_commands.rover_setups[0].rover
        tss = m.get_mocked_turn_command_selector_turn_left_from_north_command_only()
        mss = m.get_mocked_move_command_selector_north_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        final_pos = rrs.run(['M'])
        self.assertEqual(Rover(0, 1, 'N'), final_pos)

    def test_rover_runner_turns_rover_left(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = small_mars_with_one_rover_empty_commands.rover_setups[0].rover
        tss = m.get_mocked_turn_command_selector_turn_left_from_north_command_only()
        mss = m.get_mocked_move_command_selector_north_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        final_pos = rrs.run(['L'])
        self.assertEqual(Rover(0, 0, 'W'), final_pos)

    def test_rover_runner_turns_rover_right(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = small_mars_with_one_rover_empty_commands.rover_setups[0].rover
        tss = m.get_mocked_turn_command_selector_turn_right_from_north_command_only()
        mss = m.get_mocked_move_command_selector_north_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        final_pos = rrs.run(['R'])
        self.assertEqual(Rover(0, 0, 'E'), final_pos)

    def test_rover_runner_goes_off_gird_east(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = Rover(1, 1, "E")
        tss = m.get_mocked_turn_command_selector_turn_right_from_north_command_only()
        mss = m.get_mocked_move_command_selector_east_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        self.assertRaises(ValueError, rrs.run, ['M'])

    def test_rover_runner_goes_off_gird_north(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = Rover(1, 1, "N")
        tss = m.get_mocked_turn_command_selector_turn_right_from_north_command_only()
        mss = m.get_mocked_move_command_selector_north_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        self.assertRaises(ValueError, rrs.run, ['M'])

    def test_rover_runner_goes_off_gird_west(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = Rover(0, 1, "W")
        tss = m.get_mocked_turn_command_selector_turn_right_from_north_command_only()
        mss = m.get_mocked_move_command_selector_west_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        self.assertRaises(ValueError, rrs.run, ['M'])

    def test_rover_runner_goes_off_gird_south(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = Rover(0, 0, "S")
        tss = m.get_mocked_turn_command_selector_turn_right_from_north_command_only()
        mss = m.get_mocked_move_command_selector_south_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        self.assertRaises(ValueError, rrs.run, ['M'])

    def test_rover_runner_does_nothing_empty_command(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = small_mars_with_one_rover_empty_commands.rover_setups[0].rover
        tss = m.get_mocked_turn_command_selector_turn_left_from_north_command_only()
        mss = m.get_mocked_move_command_selector_north_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        final_pos = rrs.run([])
        self.assertEqual(rover, final_pos)

    def test_rover_runner_raises_error_for_None_command(self):
        grid = small_mars_with_one_rover_empty_commands.grid
        rover = small_mars_with_one_rover_empty_commands.rover_setups[0].rover
        tss = m.get_mocked_turn_command_selector_turn_left_from_north_command_only()
        mss = m.get_mocked_move_command_selector_north_command_only()
        rrs = RoverRunnerService(grid, rover, mss, tss)
        self.assertRaises(TypeError, rrs.run, None)
