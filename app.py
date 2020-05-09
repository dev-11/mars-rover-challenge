from repositories import TxtRepository
from parsers.input_parser import parse
from services.rover_runner_service import RoverRunnerService


def main():
    repo = TxtRepository()
    command_input = repo.read_file('sample_commands.txt')
    mars = parse(command_input)

    final_positions = [RoverRunnerService(mars.grid, rs.rover).run(rs.commands) for rs in mars.rover_setups]

    print(*final_positions, sep="\n")


if __name__ == '__main__':
    main()
