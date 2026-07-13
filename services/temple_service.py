from abc import ABC
from abc import abstractmethod

class TempleService(ABC):

    @abstractmethod
    def get_all_temples(self):
        pass