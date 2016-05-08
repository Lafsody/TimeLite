import random
import pprint
import math

class LearningMachine():
    def __init__(self, dataHolder):
        self.gamma = 0.8
        self.dataHolder = dataHolder

    def Init(self):
        print("LearningState")
        self.map = self.dataHolder.GetMap()
        self.height = self.map.height
        self.width = self.map.width
        self.Learn(20000)

    def Learn(self, round):
        for i in range(round):
            self.RunAI(i, round)

    def RunAI(self, round, maxRound):
        qArray = self.dataHolder.qArray
        playerPosition = (0,0)
        # pprint.pprint(qArray)
        for timeSlot in range(0, self.dataHolder.maxTimeSlot - 1):
            # actionId, nextPosition = self.RandomAction(playerPosition)
            actionId, nextPosition = self.RandomActionGreedy(playerPosition, qArray, timeSlot, round, maxRound)
            pass # Update QArray
            temp = [self.CanMove(nextPosition, id) for id in range(self.dataHolder.actionIdSize)]
            maxNextQ = max([qArray[nextPosition[0]][nextPosition[1]][timeSlot + 1][x[1]] for x in temp if x[0]])
            #qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId] = self.GetReward(nextPosition, timeSlot + 1) + int(self.gamma * maxNextQ)
            qSA = qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId]
            qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId] += self.GetReward(nextPosition, timeSlot + 1) + int(self.gamma * (maxNextQ - qSA))
            if (nextPosition == (self.height - 1, self.width - 1)):
                break
            elif (self.map.HasEnemyAt(nextPosition, timeSlot)): # PlayerDie
                break
            playerPosition = nextPosition

    def RandomAction(self, position):
        temp = [self.CanMove(position, id) for id in range(self.dataHolder.actionIdSize)]
        action = [(x[1], x[2]) for x in temp if x[0]]
        randIdx = random.randrange(len(action))
        return action[randIdx]

    def RandomActionGreedy(self, position, qArray, timeSlot, round, maxRound):
        temp = [self.CanMove(position, id) for id in range(self.dataHolder.actionIdSize)]
        possibleAction = [(x[1], x[2]) for x in temp if x[0]]
        ex = [math.exp(qArray[action[1][0]][action[1][1]][timeSlot][action[0]] / ((maxRound - round))) for action in possibleAction]
        sumEx = sum(ex)
        rand = random.uniform(0, sumEx)
        sumX = 0
        for i in range(len(possibleAction)):
            sumX += ex[i]
            if rand < sumX:
                return  possibleAction[i]
        return  possibleAction[len(possibleAction) - 1]

    def CanMove(self, position, actionId):
        dir = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
        x, y = position[0] + dir[actionId][0], position[1] + dir[actionId][1]
        return (0 <= x < self.map.height) and (0 <= y < self.map.width), actionId, (x, y)

    def GetReward(self, position, timeSlot):
        if(position[0] == self.height - 1 and position[1] == self.width - 1):
            return 1000000
        elif(self.map.HasEnemyAt(position, timeSlot)): # map.HasEnemyAt(timeSlot)
            return -1000000
        else:
            return  -10 * timeSlot