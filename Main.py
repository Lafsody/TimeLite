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

map = MapGenerator.Generate(5, 7, 12)
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

def LearnAndReset():
    learningMachine.Learn(1000)
    playerPath = learningMachine.GetPathFromQ()
    print(str(playerPath[len(playerPath) - 1]) + str(len(playerPath)))
    return  playerPath

timeSlot = 0
isReverse = False
while True:

    if not isReverse:
        if timeSlot < len(playerPath):
            enemyPosList = [enemy.GetPositionAt(timeSlot) for enemy in dataHolder.map.enemies]
            TestUI.Update(playerPath[timeSlot], enemyPosList, 80, 0.0005)
            timeSlot += 1
    elif isReverse:
        timeSlot -= 1
        if timeSlot >= 0:
            enemyPosList = [enemy.GetPositionAt(timeSlot) for enemy in dataHolder.map.enemies]
            print(timeSlot)
            TestUI.Update(playerPath[timeSlot], enemyPosList, 20, 0.0001)
        else:
            isReverse = False
            timeSlot = 0

    for event in TestUI.pygame.event.get():
        if event.type == TestUI.pygame.QUIT: TestUI.sys.exit()
        if event.type == TestUI.pygame.KEYDOWN:
            if event.key == TestUI.pygame.K_SPACE:
                isReverse = True
            elif event.key == TestUI.pygame.K_l:
                playerPath = LearnAndReset()
                timeSlot = 0
        if event.type == TestUI.pygame.MOUSEBUTTONDOWN:
            if TestUI.LearnButton.pressed(TestUI.pygame.mouse.get_pos()):
                playerPath = LearnAndReset()
                timeSlot = 0
            elif TestUI.RerunButton.pressed(TestUI.pygame.mouse.get_pos()):
                isReverse = True
