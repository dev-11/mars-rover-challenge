from abc import ABC, abstractmethod


class RotateStrategy(ABC):
    @abstractmethod
    def get_position(self):
        pass

    def get_direction(self):
        pass

    @abstractmethod
    def update(self, rover):
        pass


class RotateLeftStrategy(RotateStrategy):
    def get_direction(self):
        return 'L'


class RotateRightStrategy(RotateStrategy):
    def get_direction(self):
        return 'R'


class RotateLeftFromNorthStrategy(RotateLeftStrategy):

    def get_position(self):
        return 'N'

    def update(self, rover):
        rover.direction = 'W'
        return rover


class RotateLeftFromSouthStrategy(RotateLeftStrategy):

    def get_position(self):
        return 'S'

    def update(self, rover):
        rover.direction = 'E'
        return rover


class RotateLeftFromEastStrategy(RotateLeftStrategy):

    def get_position(self):
        return 'E'

    def update(self, rover):
        rover.direction = 'N'
        return rover


class RotateLeftFromWestStrategy(RotateLeftStrategy):

    def get_position(self):
        return 'W'

    def update(self, rover):
        rover.direction = 'S'
        return rover


class RotateRightFromNorthStrategy(RotateRightStrategy):

    def get_position(self):
        return 'N'

    def update(self, rover):
        rover.direction = 'E'
        return rover


class RotateRightFromSouthStrategy(RotateRightStrategy):

    def get_position(self):
        return 'S'

    def update(self, rover):
        rover.direction = 'W'
        return rover


class RotateRightFromEastStrategy(RotateRightStrategy):

    def get_position(self):
        return 'E'

    def update(self, rover):
        rover.direction = 'S'
        return rover


class RotateRightFromWestStrategy(RotateRightStrategy):

    def get_position(self):
        return 'W'

    def update(self, rover):
        rover.direction = 'N'
        return rover


def get_rotation_strategies():
    return [
        # left strategies
        RotateLeftFromNorthStrategy(),
        RotateLeftFromWestStrategy(),
        RotateLeftFromEastStrategy(),
        RotateLeftFromSouthStrategy(),
        # right strategies
        RotateRightFromNorthStrategy(),
        RotateRightFromWestStrategy(),
        RotateRightFromEastStrategy(),
        RotateRightFromSouthStrategy()

    ]

