from State import State
from State import GameState
from State import MenuState
from State import GenerateState
from Game import  Map
from Game import MapGenerator
from time import sleep
import pprint

def InitMap():
    #If have file
    pass
    #else generate new map by default
    map = MapGenerator.Generate(10, 10, 3)

def SetMap(targetMap):
    map = targetMap
    #save to file
    pass

def GetMap():
    if (map == None):
        InitMap()
    if (map == None):
       print("InitMap Not working")
    return  map

# -------------- Code Run Here -----------------------
menuState = MenuState.MenuState()
gameState = GameState.GameState()
generateState = GenerateState.GenerateState()

currentState = gameState

map = None
InitMap()

QArray = None

currentState.Init()

while True:
    sleep(0.1)
    currentState.Update()

