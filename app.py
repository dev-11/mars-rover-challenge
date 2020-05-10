from repositories import TxtRepository
from parsers.input_parser import parse
from services.rover_runner_service import RoverRunnerService
from services.move_strategies import MoveStrategySelector
from services.turn_strategies import TurnStrategySelector
import config


def main():
    repo = TxtRepository()
    command_input = repo.read_file(config.default_input_file)
    mars = parse(command_input)

    move_strategy_selector = MoveStrategySelector()
    turn_strategy_selector = TurnStrategySelector()
    final_positions = [RoverRunnerService(mars.grid, rs.rover, move_strategy_selector, turn_strategy_selector).run(rs.commands)
                       for rs in mars.rover_setups]

    print(*final_positions, sep="\n")


if __name__ == '__main__':
    main()
