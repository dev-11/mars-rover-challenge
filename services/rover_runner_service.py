class RoverRunnerService:
    def __init__(self, grid, rover):
        self._grid = grid
        self._rover = rover

    def run(self, commands: []):

        for command in commands:
            if command != 'M':
                self.update_direction(command)
            else:
                self.update_position()
                if not (0 <= self._rover.y <= self._grid.max_y) or not (0 <= self._rover.x <= self._grid.max_x):
                    raise ValueError(f"We drove the rover off-grid: {self._rover}")

        return self._rover

    def update_direction(self, command: chr):
        if command == 'L':
            if self._rover.direction == 'N':
                self._rover.direction = 'W'
            elif self._rover.direction == 'S':
                self._rover.direction = 'E'
            elif self._rover.direction == 'E':
                self._rover.direction = 'N'
            else:
                self._rover.direction = 'S'
        else:
            if self._rover.direction == 'N':
                self._rover.direction = 'E'
            elif self._rover.direction == 'S':
                self._rover.direction = 'W'
            elif self._rover.direction == 'E':
                self._rover.direction = 'S'
            else:
                self._rover.direction = 'N'

    def update_position(self):
        if self._rover.direction == 'N':
            self._rover.y += 1
        elif self._rover.direction == 'S':
            self._rover.y -= 1
        elif self._rover.direction == 'E':
            self._rover.x += 1
        else:
            self._rover.x -= 1
