from services.move_commands import MoveCommandSelector
from services.turn_commands import TurnCommandSelector
from data_objects import Grid, Rover


class RoverRunnerService:
    def __init__(self, grid: Grid, rover: Rover,
                 move_command_selector: MoveCommandSelector,
                 turn_commands_selector: TurnCommandSelector):
        self._grid = grid
        self._rover = rover
        self._move_command_selector = move_command_selector
        self._turn_commands_selector = turn_commands_selector

    def run(self, commands: []):

        for command_name in commands:
            if command_name == 'M':
                command = self._move_command_selector.get_command(self._rover.cardinal_direction)
            else:
                command = self._turn_commands_selector.get_command(self._rover.cardinal_direction, command_name)

            updated_rover = command.execute(self._rover)

            if not (0 <= updated_rover.y <= self._grid.max_y) or not (0 <= updated_rover.x <= self._grid.max_x):
                raise ValueError(f"Can't drive the rover off the grid: {updated_rover}")
            else:
                self._rover = updated_rover

        return self._rover
