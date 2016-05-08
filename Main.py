from State import State
from State import GameState
from State import MenuState
from State import GenerateState
from Game import  Map
from Game import MapGenerator
from time import sleep
from Data import DataHolder
from Game import LearningMachine
import pprint

# -------------- Code Run Here -----------------------
dataHolder = DataHolder.DataHolder()
learningMachine = LearningMachine.LearningMachine(dataHolder)

map = MapGenerator.Generate(10, 10, 10)
dataHolder.SetMap(map)
learningMachine.Init()
pprint.pprint(dataHolder.GetQArray())

menuState = MenuState.MenuState(dataHolder)
gameState = GameState.GameState(dataHolder)
generateState = GenerateState.GenerateState(dataHolder)

currentState = gameState

currentState.Init()

while True:
    sleep(0.1)
    # currentState.Update()

