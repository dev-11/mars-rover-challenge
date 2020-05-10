from abc import ABC, abstractmethod


class TurnStrategy(ABC):
    @abstractmethod
    def get_cardinal_direction(self):
        pass

    @abstractmethod
    def get_turning_direction(self):
        pass

    @abstractmethod
    def update(self, rover):
        pass


class TurnLeftStrategy(TurnStrategy):
    def get_turning_direction(self):
        return 'L'


class TurnRightStrategy(TurnStrategy):
    def get_turning_direction(self):
        return 'R'


class TurnLeftFromNorthStrategy(TurnLeftStrategy):

    def get_cardinal_direction(self):
        return 'N'

    def update(self, rover):
        rover.cardinal_direction = 'W'
        return rover


class TurnLeftFromSouthStrategy(TurnLeftStrategy):

    def get_cardinal_direction(self):
        return 'S'

    def update(self, rover):
        rover.cardinal_direction = 'E'
        return rover


class TurnLeftFromEastStrategy(TurnLeftStrategy):

    def get_cardinal_direction(self):
        return 'E'

    def update(self, rover):
        rover.cardinal_direction = 'N'
        return rover


class TurnLeftFromWestStrategy(TurnLeftStrategy):

    def get_cardinal_direction(self):
        return 'W'

    def update(self, rover):
        rover.cardinal_direction = 'S'
        return rover


class TurnRightFromNorthStrategy(TurnRightStrategy):

    def get_cardinal_direction(self):
        return 'N'

    def update(self, rover):
        rover.cardinal_direction = 'E'
        return rover


class TurnRightFromSouthStrategy(TurnRightStrategy):

    def get_cardinal_direction(self):
        return 'S'

    def update(self, rover):
        rover.cardinal_direction = 'W'
        return rover


class TurnRightFromEastStrategy(TurnRightStrategy):

    def get_cardinal_direction(self):
        return 'E'

    def update(self, rover):
        rover.cardinal_direction = 'S'
        return rover


class TurnRightFromWestStrategy(TurnRightStrategy):

    def get_cardinal_direction(self):
        return 'W'

    def update(self, rover):
        rover.cardinal_direction = 'N'
        return rover


def get_turn_strategies():
    return [
        # left strategies
        TurnLeftFromNorthStrategy(),
        TurnLeftFromWestStrategy(),
        TurnLeftFromEastStrategy(),
        TurnLeftFromSouthStrategy(),
        # right strategies
        TurnRightFromNorthStrategy(),
        TurnRightFromWestStrategy(),
        TurnRightFromEastStrategy(),
        TurnRightFromSouthStrategy()

    ]

