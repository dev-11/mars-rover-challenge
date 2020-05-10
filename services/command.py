from abc import ABC, abstractmethod
from data_objects import Rover


class Command(ABC):
    @abstractmethod
    def execute(self, rover: Rover):
        pass
