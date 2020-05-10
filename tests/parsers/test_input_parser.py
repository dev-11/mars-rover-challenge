import unittest
from parsers import input_parser
from tests.test_environment import marses
import data_objects as do


class TestInputParser(unittest.TestCase):
    def test_parse_returns_correct_data_for_sample_commands(self):
        commands = ['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM']
        mars = input_parser.parse(commands)
        self.assertEqual(marses.default_mars, mars)

    def test_parse_returns_correct_data_for_lower_case_sample_commands(self):
        commands = ['5 5', '1 2 N', 'lmlmlmlmm', '3 3 E', 'mmrmmrmrrm']
        mars = input_parser.parse(commands)
        self.assertEqual(marses.default_mars, mars)

    def test_parse_raises_IndexError_for_empty_input(self):
        commands = []
        self.assertRaises(IndexError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_empty_grid_data(self):
        commands = ['']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_incomplete_and_invalid_grid_data(self):
        commands = ['A']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_incomplete_grid_data(self):
        commands = ['1']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_invalid_grid_data_max_x(self):
        commands = ['A 1']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_invalid_grid_data_max_y(self):
        commands = ['1 B']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_extra_value_in_grid_data(self):
        commands = ['1 1 1']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_empty_rover_data(self):
        commands = ['5 5', '']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_invalid_rover_x_coordinate(self):
        commands = ['5 5', '1 B C']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_invalid_rover_y_coordinate(self):
        commands = ['5 5', 'A 2 C']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_ValueError_for_extra_value_for_rover(self):
        commands = ['5 5', 'A 2 C 1']
        self.assertRaises(ValueError, input_parser.parse, commands)

    def test_parse_raises_TypeError_for_None_rover_commands(self):
        commands = ['5 5', '1 1 C', None]
        self.assertRaises(AttributeError, input_parser.parse, commands)

    def test_parse_return_mars_data_with_empty_rover_commands(self):
        commands = ['5 5', '1 1 C', '']
        mars = input_parser.parse(commands)
        self.assertEqual(do.Mars(do.Grid(5, 5), [do.RoverSetup(do.Rover(1, 1, 'C'), [])]), mars)
