from repositories import TxtRepository
from parsers.input_parser import parse
from services.rover_runner_service import RoverRunnerService
from services.move_strategies import get_move_strategies
from services.turn_strategies import get_turn_strategies
import config


def main():
    repo = TxtRepository()
    command_input = repo.read_file(config.default_input_file)
    mars = parse(command_input)

    move_strategies = get_move_strategies()
    turn_strategies = get_turn_strategies()
    final_positions = [RoverRunnerService(mars.grid, rs.rover, move_strategies, turn_strategies).run(rs.commands)
                       for rs in mars.rover_setups]

    print(*final_positions, sep="\n")


if __name__ == '__main__':
    main()
