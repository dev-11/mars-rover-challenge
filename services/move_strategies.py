from data_objects import Rover
from abc import ABC, abstractmethod


class MoveStrategy(ABC):
    @abstractmethod
    def get_cardinal_direction(self):
        pass

    @abstractmethod
    def update(self, rover: Rover):
        pass


class MoveToNorthStrategy(MoveStrategy):
    def get_cardinal_direction(self):
        return 'N'

    def update(self, rover: Rover):
        rover.y += 1
        return rover


class MoveToSouthStrategy(MoveStrategy):
    def get_cardinal_direction(self):
        return 'S'

    def update(self, rover: Rover):
        rover.y -= 1
        return rover


class MoveToEastStrategy(MoveStrategy):
    def get_cardinal_direction(self):
        return 'E'

    def update(self, rover: Rover):
        rover.x += 1
        return rover


class MoveToWestStrategy(MoveStrategy):
    def get_cardinal_direction(self):
        return 'W'

    def update(self, rover: Rover):
        rover.x -= 1
        return rover


def get_move_strategies():
    return [
        MoveToNorthStrategy(),
        MoveToSouthStrategy(),
        MoveToEastStrategy(),
        MoveToWestStrategy()
    ]
