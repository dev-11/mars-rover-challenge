from dataclasses import dataclass


@dataclass
class Grid:
    max_x: int
    max_y: int


@dataclass
class Rover:
    x: int
    y: int
    direction: chr

    def __str__(self):
        return f'{self.x} {self.y} {self.direction}'


@dataclass
class RoverSetup:
    rover: Rover
    commands: []


@dataclass
class Mars:
    grid: Grid
    rover_setups: []
