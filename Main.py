from State import State
from State import GameState
from Game import  Map
from time import sleep

currentState =  GameState.GameState()
map = None

currentState.Reset()

while True:
    sleep(0.1)
    currentState.Update()

