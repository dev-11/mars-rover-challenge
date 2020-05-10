from abc import ABC, abstractmethod
import copy


class TurnCommand(ABC):
    @abstractmethod
    def get_cardinal_direction(self):
        pass

    @abstractmethod
    def get_turning_direction(self):
        pass

    @abstractmethod
    def execute(self, rover):
        pass


class TurnLeftCommand(TurnCommand):
    def get_turning_direction(self):
        return 'L'


class TurnRightCommand(TurnCommand):
    def get_turning_direction(self):
        return 'R'


class TurnLeftFromNorthCommand(TurnLeftCommand):

    def get_cardinal_direction(self):
        return 'N'

    def execute(self, rover):
        updated_rover = copy.copy(rover)
        updated_rover.cardinal_direction = 'W'
        return updated_rover


class TurnLeftFromSouthCommand(TurnLeftCommand):

    def get_cardinal_direction(self):
        return 'S'

    def execute(self, rover):
        updated_rover = copy.copy(rover)
        updated_rover.cardinal_direction = 'E'
        return updated_rover


class TurnLeftFromEastCommand(TurnLeftCommand):

    def get_cardinal_direction(self):
        return 'E'

    def execute(self, rover):
        updated_rover = copy.copy(rover)
        updated_rover.cardinal_direction = 'N'
        return updated_rover


class TurnLeftFromWestCommand(TurnLeftCommand):

    def get_cardinal_direction(self):
        return 'W'

    def execute(self, rover):
        updated_rover = copy.copy(rover)
        updated_rover.cardinal_direction = 'S'
        return updated_rover


class TurnRightFromNorthCommand(TurnRightCommand):

    def get_cardinal_direction(self):
        return 'N'

    def execute(self, rover):
        updated_rover = copy.copy(rover)
        updated_rover.cardinal_direction = 'E'
        return updated_rover


class TurnRightFromSouthCommand(TurnRightCommand):

    def get_cardinal_direction(self):
        return 'S'

    def execute(self, rover):
        updated_rover = copy.copy(rover)
        updated_rover.cardinal_direction = 'W'
        return updated_rover


class TurnRightFromEastCommand(TurnRightCommand):

    def get_cardinal_direction(self):
        return 'E'

    def execute(self, rover):
        updated_rover = copy.copy(rover)
        updated_rover.cardinal_direction = 'S'
        return updated_rover


class TurnRightFromWestCommand(TurnRightCommand):

    def get_cardinal_direction(self):
        return 'W'

    def execute(self, rover):
        updated_rover = copy.copy(rover)
        updated_rover.cardinal_direction = 'N'
        return updated_rover


def get_turn_commands():
    return [
        # left commands
        TurnLeftFromNorthCommand(),
        TurnLeftFromWestCommand(),
        TurnLeftFromEastCommand(),
        TurnLeftFromSouthCommand(),
        # right commands
        TurnRightFromNorthCommand(),
        TurnRightFromWestCommand(),
        TurnRightFromEastCommand(),
        TurnRightFromSouthCommand()

    ]


class TurnCommandSelector:
    def __init__(self):
        self._strategies = get_turn_commands()

    def get_command(self, cardinal_direction: chr, turning_direction: chr):
        return list(filter(lambda s: s.get_turning_direction() == turning_direction
                                     and s.get_cardinal_direction() == cardinal_direction,
                           self._strategies))[0]