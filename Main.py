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

map = MapGenerator.Generate(5, 7, 10)
dataHolder.SetMap(map)
learningMachine.Init()
pprint.pprint(dataHolder.GetQArray())

menuState = MenuState.MenuState(dataHolder)
gameState = GameState.GameState(dataHolder)
generateState = GenerateState.GenerateState(dataHolder)

currentState = gameState

currentState.Init()

from UI import TestUI
# print(TestUI.size)
# TestUI.init(5, 10, 15)
# print(TestUI.size)

TestUI.Init(dataHolder.map.width, dataHolder.map.height, len(dataHolder.map.enemies))
playerPath = learningMachine.GetPathFromQ()
print (len(playerPath))
print (playerPath)

timeSlot = 0
while True:
    if timeSlot < len(playerPath):
        enemyPosList = [enemy.GetPositionAt(timeSlot) for enemy in dataHolder.map.enemies]
        TestUI.Update(playerPath[timeSlot], enemyPosList)
        timeSlot += 1

    for event in TestUI.pygame.event.get():
        if event.type == TestUI.pygame.QUIT: TestUI.sys.exit()
        if event.type == TestUI.pygame.KEYDOWN:
            if event.key == TestUI.pygame.K_SPACE:
                timeSlot = 0
            elif event.key == TestUI.pygame.K_l:
                learningMachine.Learn(1000)
                playerPath = learningMachine.GetPathFromQ()
                print(str(playerPath[len(playerPath) - 1]) + str(len(playerPath)))
                timeSlot = 0
