from State import State
from Game import Map
from Game import MapGenerator

class GenerateState(State.State):
    def __init__(self, dataHolder):
        self.dataHolder = dataHolder

    def Init(self):
        print("GenerateState")
        map = MapGenerator.Generate(10, 10, 3)
        self.dataHolder.SetMap(map)

    def Update(self):
        pass