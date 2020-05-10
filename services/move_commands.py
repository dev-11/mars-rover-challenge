from data_objects import Rover
from services.command import Command
from abc import abstractmethod
from copy import copy


class MoveCommand(Command):
    @abstractmethod
    def get_cardinal_direction(self):
        pass


class MoveToNorthCommand(MoveCommand):
    def get_cardinal_direction(self):
        return 'N'

    def execute(self, rover: Rover):
        updated = copy(rover)
        updated.y += 1
        return updated


class MoveToSouthCommand(MoveCommand):
    def get_cardinal_direction(self):
        return 'S'

    def execute(self, rover: Rover):
        updated = copy(rover)
        updated.y -= 1
        return updated


class MoveToEastCommand(MoveCommand):
    def get_cardinal_direction(self):
        return 'E'

    def execute(self, rover: Rover):
        updated = copy(rover)
        updated.x += 1
        return updated


class MoveToWestCommand(MoveCommand):
    def get_cardinal_direction(self):
        return 'W'

    def execute(self, rover: Rover):
        updated = copy(rover)
        updated.x -= 1
        return updated


def get_move_commands():
    return [
        MoveToNorthCommand(),
        MoveToSouthCommand(),
        MoveToEastCommand(),
        MoveToWestCommand()
    ]


class MoveCommandSelector:
    def __init__(self):
        self._strategies = get_move_commands()

    def select(self, cardinal_direction: chr):
        return list(filter(lambda s: s.get_cardinal_direction() == cardinal_direction,
                    self._strategies))[0]
