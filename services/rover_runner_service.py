class RoverRunnerService:
    def __init__(self, grid, rover, move_strategies, turn_strategies):
        self._grid = grid
        self._rover = rover
        self._move_strategies = move_strategies
        self._turn_strategies = turn_strategies

    def run(self, commands: []):

        for command in commands:
            if command != 'M':
                strategy = list(filter(lambda s: s.get_turning_direction() == command
                                                 and s.get_cardinal_direction() == self._rover.cardinal_direction,
                                       self._turn_strategies))[0]
            else:
                strategy = list(filter(lambda s: s.get_cardinal_direction() == self._rover.cardinal_direction,
                                       self._move_strategies))[0]

            updated_rover = strategy.update(self._rover)

            if not (0 <= updated_rover.y <= self._grid.max_y) or not (0 <= updated_rover.x <= self._grid.max_x):
                raise ValueError(f"Can't drove the rover off the grid: {updated_rover}")
            else:
                self._rover = updated_rover

        return self._rover
