from services.move_strategies import MoveStrategySelector
from services.turn_strategies import TurnStrategySelector
from data_objects import Grid, Rover


class RoverRunnerService:
    def __init__(self, grid: Grid, rover: Rover,
                 move_strategy_selector: MoveStrategySelector,
                 turn_strategy_selector: TurnStrategySelector):
        self._grid = grid
        self._rover = rover
        self._move_strategy_selector = move_strategy_selector
        self._turn_strategy_selector = turn_strategy_selector

    def run(self, commands: []):

        for command in commands:
            if command == 'M':
                strategy = self._move_strategy_selector.get_strategy(self._rover.cardinal_direction)
            else:
                strategy = self._turn_strategy_selector.get_strategy(self._rover.cardinal_direction, command)

            updated_rover = strategy.update(self._rover)

            if not (0 <= updated_rover.y <= self._grid.max_y) or not (0 <= updated_rover.x <= self._grid.max_x):
                raise ValueError(f"Can't drove the rover off the grid: {updated_rover}")
            else:
                self._rover = updated_rover

        return self._rover
