from abc import ABC
from abc import abstractmethod

class TempleRepository(ABC):

    @abstractmethod
    def get_all_temples(self):
        pass