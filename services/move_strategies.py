from data_objects import Rover
from abc import ABC, abstractmethod
from copy import copy


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
        updated = copy(rover)
        updated.y += 1
        return updated


class MoveToSouthStrategy(MoveStrategy):
    def get_cardinal_direction(self):
        return 'S'

    def update(self, rover: Rover):
        updated = copy(rover)
        updated.y -= 1
        return updated


class MoveToEastStrategy(MoveStrategy):
    def get_cardinal_direction(self):
        return 'E'

    def update(self, rover: Rover):
        updated = copy(rover)
        updated.x += 1
        return updated


class MoveToWestStrategy(MoveStrategy):
    def get_cardinal_direction(self):
        return 'W'

    def update(self, rover: Rover):
        updated = copy(rover)
        updated.x -= 1
        return updated


def get_move_strategies():
    return [
        MoveToNorthStrategy(),
        MoveToSouthStrategy(),
        MoveToEastStrategy(),
        MoveToWestStrategy()
    ]


class MoveStrategySelector:
    def __init__(self):
        self._strategies = get_move_strategies()

    def get_strategy(self, cardinal_direction: chr):
        return list(filter(lambda s: s.get_cardinal_direction() == cardinal_direction,
                    self._strategies))[0]
