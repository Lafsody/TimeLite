from abc import ABC, abstractmethod

class State(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def Init(self):
        pass

    @abstractmethod
    def Update(self):
        pass