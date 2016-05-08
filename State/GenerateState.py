from State import State
from Game import Map
from Game import MapGenerator
import Main

class GenerateState(State.State):
    def __init__(self):
        pass

    def Init(self):
        print("GenerateState")
        map = MapGenerator.Generate(10, 10, 3)
        Main.SetMap(map)

    def Update(self):
        pass