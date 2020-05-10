from repositories import TxtRepository
from parsers.input_parser import parse
from services.rover_runner_service import RoverRunnerService
from services.move_commands import MoveCommandSelector
from services.turn_commands import TurnCommandSelector
import config
import sys
import getopt


def get_input_file_path(argv):
    input_file = config.default_input_file
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile="])
    except getopt.GetoptError:
        print('app.py -i <input_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('app.py -i <input_file>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
    return input_file


def main(file_path):
    repo = TxtRepository()
    command_input = repo.read_file(file_path)
    mars = parse(command_input)

    move_command_selector = MoveCommandSelector()
    turn_command_selector = TurnCommandSelector()
    final_positions = [RoverRunnerService(mars.grid, rs.rover, move_command_selector, turn_command_selector).run(rs.commands)
                       for rs in mars.rover_setups]

    print(*final_positions, sep="\n")


if __name__ == '__main__':
    file = get_input_file_path(sys.argv[1:])
    main(file)


