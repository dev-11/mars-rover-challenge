import unittest
from parsers import input_parser
import data_objects as do


class TestInputParser(unittest.TestCase):
    def test_parse_return_correct_data_for_sample_commands(self):
        commands = [
            '5 5',
            '1 2 N',
            'LMLMLMLMM',
            '3 3 E',
            'MMRMMRMRRM'
        ]
        mars = input_parser.parse(commands)
        self.assertEqual(
            do.Mars(do.Grid(5, 5), [
                do.RoverSetup(do.Rover(1, 2, 'N'), ['L', 'M', 'L', 'M', 'L', 'M', 'L', 'M', 'M']),
                do.RoverSetup(do.Rover(3, 3, 'E'), ['M', 'M', 'R', 'M', 'M', 'R', 'M', 'R', 'R', 'M'])
            ]),
            mars
        )
