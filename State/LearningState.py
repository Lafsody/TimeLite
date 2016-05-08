from State import State
from Game import Map
from Game import MapGenerator
import random
import Main

class LearningState(State.State):
    def __init__(self):
        self.gamma = 0.3

    def Init(self):
        print("LearningState")
        self.map = Main.GetMap()
        self.height = map.height
        self.width = map.width
        self.maxTimeSlot = 1000
        self.action = 5
        self.QArray = [[[[0 for l in range(self.height)] for k in range(self.width)] for j in range(self.maxTimeSlot)] for i in range(self.action)]
        self.Learn()

    def Update(self):
        pass

    def Learn(self):
        for i in range(100000):
            self.RunAI()

    def RunAI(self):
        playerPosition = (0,0)
        for timeSlot in range(1, self.maxTimeSlot):
            actionId, nextPosition = self.RandomAction(playerPosition)
            pass # Update QArray
            # self.QArray[nextPosition[0]][nextPosition[1]][timeSlot][actionId] = self.GetReward(nextPosition, timeSlot) + int(self.gamma * FindMax(NextState))
            if (nextPosition == (self.height, self.width)):
                break
            elif (False): # PlayerDie
                break
            playerPosition = nextPosition

    def RandomAction(self, position):
        action = []
        # 0 idle
        action.append(0)
        # 1 Up
        # 2 Right
        # 3 Down
        # 4 Left
        actionId = random.randrange(len(action))
        nextPosition = (position[0], position[1])
        return actionId, nextPosition

    def GetReward(self, position, timeSlot):
        if(position[0] == self.height - 1 and position[1] == self.width):
            return 10000
        elif(self.map.HasEnemyAt(position, timeSlot)): # map.HasEnemyAt(timeSlot)
            return -1000000
        else:
            return  -10