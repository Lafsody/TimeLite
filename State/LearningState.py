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
        self.height = self.map.height
        self.width = self.map.width
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
            temp = [self.CanMove(nextPosition, id) for id in range(5)]
            maxNextQ = max([self.QArray[x[2][0]][x[2][1]][timeSlot + 1][x[1]] for x in temp if x[0]])
            self.QArray[nextPosition[0]][nextPosition[1]][timeSlot][actionId] = self.GetReward(nextPosition, timeSlot) + int(self.gamma * maxNextQ)
            if (nextPosition == (self.height - 1, self.width - 1)):
                break
            elif (self.map.HasEnemyAt(nextPosition, timeSlot)): # PlayerDie
                break
            playerPosition = nextPosition

    def RandomAction(self, position):
        temp = [self.CanMove(position, id) for id in range(5)]
        action = [(x[1], x[2]) for x in temp if x[0]]
        randIdx = random.randrange(len(action))
        return action[randIdx]

    def CanMove(self, position, actionId):
        dir = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
        x, y = position[0] + dir[actionId][0], position[1] + dir[actionId][1]
        return (x in range(self.map.height) and y in range(self.map.width)), actionId, (x, y)

    def GetReward(self, position, timeSlot):
        if(position[0] == self.height - 1 and position[1] == self.width):
            return 1000000
        elif(self.map.HasEnemyAt(position, timeSlot)): # map.HasEnemyAt(timeSlot)
            return -1000000
        else:
            return  -10