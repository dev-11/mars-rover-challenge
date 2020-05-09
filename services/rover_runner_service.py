class RoverRunnerService:
    def __init__(self, grid, rover, move_strategies, rotate_strategies):
        self._grid = grid
        self._rover = rover
        self._move_strategies = move_strategies
        self._rotate_strategies = rotate_strategies

    def run(self, commands: []):

        for command in commands:
            if command != 'M':
                strategy = list(filter(lambda s: s.get_direction() == command
                            and s.get_position() == self._rover.direction, self._rotate_strategies))[0]
            else:
                strategy = list(filter(lambda s: s.get_direction() == self._rover.direction, self._move_strategies))[0]

            self._rover = strategy.update(self._rover)

            if not (0 <= self._rover.y <= self._grid.max_y) or not (0 <= self._rover.x <= self._grid.max_x):
                raise ValueError(f"We drove the rover off the grid: {self._rover}")

        return self._rover
