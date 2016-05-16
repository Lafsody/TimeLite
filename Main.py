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

def GenerateMap():
    global map, dataHolder, playerPath
    map = MapGenerator.Generate(5, 7, 15)
    dataHolder.SetMap(map)
    learningMachine.Init()
    playerPath = learningMachine.GetPathFromQ()

GenerateMap()
pprint.pprint(dataHolder.GetQArray())

menuState = MenuState.MenuState(dataHolder)
# gameState = GameState.GameState(dataHolder)
# generateState = GenerateState.GenerateState(dataHolder)

# currentState = gameState

# currentState.Init()

from UI import TestUI
# print(TestUI.size)
# TestUI.init(5, 10, 15)
# print(TestUI.size)

TestUI.Init(dataHolder.map.width, dataHolder.map.height, len(dataHolder.map.enemies))
playerPath = learningMachine.GetPathFromQ()
print (len(playerPath))
print (playerPath)

timeSlot = 0
isReverse = False

TestUI.timeline.SetMaxTimeSlot(len(playerPath))

def SetTimeSlot(_timeSlot):
    global timeSlot
    timeSlot = _timeSlot
    TestUI.timeline.SetCurrentTimeSlot(_timeSlot)

def LearnAndReset():
    learningMachine.Learn(1000)
    global playerPath, timeSlot
    playerPath = learningMachine.GetPathFromQ()
    SetTimeSlot(0)
    TestUI.timeline.SetMaxTimeSlot(len(playerPath))
    print(str(playerPath[len(playerPath) - 1]) + str(len(playerPath)))

while True:
    if not isReverse:
        if timeSlot < len(playerPath):
            enemyPosList = [enemy.GetPositionAt(timeSlot) for enemy in dataHolder.map.enemies]
            TestUI.Update(playerPath[timeSlot], enemyPosList, 80, 0.0005)
            SetTimeSlot(timeSlot + 1)
    elif isReverse:
        SetTimeSlot(timeSlot - 1)
        if timeSlot >= 0:
            enemyPosList = [enemy.GetPositionAt(timeSlot) for enemy in dataHolder.map.enemies]
            TestUI.Update(playerPath[timeSlot], enemyPosList, 20, 0.0001)
        else:
            isReverse = False
            SetTimeSlot(0)

    for event in TestUI.pygame.event.get():
        if event.type == TestUI.pygame.QUIT: TestUI.sys.exit()
        if event.type == TestUI.pygame.KEYDOWN:
            if event.key == TestUI.pygame.K_SPACE:
                isReverse = True
            elif event.key == TestUI.pygame.K_l:
                LearnAndReset()
        if event.type == TestUI.pygame.MOUSEBUTTONDOWN:
            if TestUI.LearnButton.pressed(TestUI.pygame.mouse.get_pos()):
                LearnAndReset()
            elif TestUI.ReGenerateButton.pressed(TestUI.pygame.mouse.get_pos()):
                GenerateMap()
                TestUI.timeline.SetMaxTimeSlot(len(playerPath))
                isReverse = False
                SetTimeSlot(0)
            elif TestUI.RerunButton.pressed(TestUI.pygame.mouse.get_pos()):
                isReverse = True
            if TestUI.timeline.knob.collidepoint(event.pos):
                TestUI.timeline.SetScrolling(True)
        elif (event.type == TestUI.pygame.MOUSEMOTION and TestUI.timeline.scrolling):
            if event.rel[0] != 0:
                move = max(event.rel[0], TestUI.timeline.track.left - TestUI.timeline.knob.left)
                move = min(move, TestUI.timeline.track.right - TestUI.timeline.knob.right)

                if move != 0:
                    TestUI.timeline.knob.move_ip((move, 0))
        elif event.type == TestUI.pygame.MOUSEBUTTONUP:
            TestUI.timeline.SetScrolling(False)
