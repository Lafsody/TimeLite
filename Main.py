from Game import MapGenerator
from Data import DataHolder
from Game import LearningMachine
import pprint

# -------------- Code Run Here -----------------------

# dataHolder collect a q-map,freq-map,and states that have reach
dataHolder = DataHolder.DataHolder()

# Learning Machine is use to update q-map value by Q-Learning
learningMachine = LearningMachine.LearningMachine(dataHolder)

# get set of paths from maximum Q in each state
def GetPlayerPath():
    global playerPath
    playerPath = learningMachine.GetPathFromQ()
    print(str(playerPath[len(playerPath) - 1]) + str(len(playerPath)))

# This function is use to generate map and enemy
def GenerateMap():
    global map, dataHolder, playerPath
    # Generate Map with height,width,numOfEnemy
    map = MapGenerator.Generate(5, 7, 15)
    dataHolder.SetMap(map)
    learningMachine.Init()
    GetPlayerPath()

GenerateMap()
pprint.pprint(dataHolder.GetQArray())

from UI import TestUI
# print(TestUI.size)
# TestUI.init(5, 10, 15)
# print(TestUI.size)

# Instantiate UI
TestUI.Init(dataHolder.map.width, dataHolder.map.height, len(dataHolder.map.enemies))

GetPlayerPath()

timeSlot = 0
isReverse = False

TestUI.timeline.SetMaxTimeSlot(len(playerPath))

def SetTimeSlot(_timeSlot):
    global timeSlot
    timeSlot = _timeSlot
    TestUI.timeline.SetCurrentTimeSlot(_timeSlot)

def LearnAndReset():
    # Learn and Get new path
    # input iteration of run
    learningMachine.Learn(1000)
    global playerPath, timeSlot
    GetPlayerPath()
    SetTimeSlot(0)
    TestUI.timeline.SetMaxTimeSlot(len(playerPath))

while True:
    if not isReverse:
        if timeSlot < len(playerPath):
            enemyPosList = [enemy.GetPositionAt(timeSlot) for enemy in dataHolder.map.enemies]
            # knobX is use on timeline that already remove
            knobX = TestUI.timeline.GetKnobPositionAtTimeSlot(timeSlot)
            TestUI.Update(playerPath[timeSlot], enemyPosList, knobX, 80, 0.0005)
            SetTimeSlot(timeSlot + 1)
    elif isReverse:
        # Enter This when rerun
        SetTimeSlot(timeSlot - 1)
        if timeSlot >= 0:
            enemyPosList = [enemy.GetPositionAt(timeSlot) for enemy in dataHolder.map.enemies]
            # knobX is use on timeline that already remove
            knobX = TestUI.timeline.GetKnobPositionAtTimeSlot(timeSlot)
            TestUI.Update(playerPath[timeSlot], enemyPosList, knobX, 20, 0.0001)
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
            # Learn+ Button
            if TestUI.LearnButton.pressed(TestUI.pygame.mouse.get_pos()):
                LearnAndReset()
            # ReGenerate Button
            elif TestUI.ReGenerateButton.pressed(TestUI.pygame.mouse.get_pos()):
                GenerateMap()
                TestUI.timeline.SetMaxTimeSlot(len(playerPath))
                isReverse = False
                SetTimeSlot(0)
            #Rerun Button
            elif TestUI.RerunButton.pressed(TestUI.pygame.mouse.get_pos()):
                isReverse = True
            # ---- This Is Timeline Code ---- But Animation does not work well so we remove it out
            # if TestUI.timeline.knob.collidepoint(event.pos):
            #     TestUI.timeline.SetScrolling(True)
        # elif (event.type == TestUI.pygame.MOUSEMOTION and TestUI.timeline.scrolling):
        #     if event.rel[0] != 0:
        #         move = max(event.rel[0], TestUI.timeline.track.left - TestUI.timeline.knob.left)
        #         move = min(move, TestUI.timeline.track.right - TestUI.timeline.knob.right)
        #
        #         if move != 0:
        #             TestUI.timeline.knob.move_ip((move, 0))
        # elif event.type == TestUI.pygame.MOUSEBUTTONUP:
        #     TestUI.timeline.SetScrolling(False)
