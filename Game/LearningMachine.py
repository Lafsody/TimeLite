import random
import pprint
import math

class LearningMachine():
    def __init__(self, dataHolder):
        self.gamma = 0.7
        self.dataHolder = dataHolder

    def Init(self):
        print("LearningState")
        self.map = self.dataHolder.GetMap()
        self.height = self.map.height
        self.width = self.map.width
        self.Learn(3000)

    def Learn(self, round):
        for i in range(round):
            self.RunAI(i, round)

    def RunAI(self, round, maxRound):
        qArray = self.dataHolder.qArray
        playerPosition = (0,0)
        # pprint.pprint(qArray)
        for timeSlot in range(0, self.dataHolder.maxTimeSlot - 1):
            # actionId, nextPosition = self.RandomAction(playerPosition)
            # actionId, nextPosition = self.RandomActionGreedy(playerPosition, qArray, timeSlot, round, maxRound)
            # actionId, nextPosition = self.RandomActionSimpleGreedy(playerPosition, qArray, timeSlot, round, maxRound)
            actionId, nextPosition = self.RandomActionGreedy2(playerPosition, timeSlot)
            pass # Update QArray
            temp = [self.CanMove(nextPosition, id, timeSlot) for id in range(self.dataHolder.actionIdSize)]
            maxNextQ = max([qArray[nextPosition[0]][nextPosition[1]][timeSlot + 1][x[1]] for x in temp if x[0]])
            newQValue = self.GetReward2(nextPosition, timeSlot + 1) + int(self.gamma * maxNextQ)
            oldQValue = qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId]
            # qSA = qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId]
            # newQValue = qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId] + self.GetReward2(nextPosition, timeSlot + 1) + int(self.gamma * (maxNextQ - qSA))
            if oldQValue < newQValue or oldQValue == 0:
                qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId] = newQValue
            self.dataHolder.freqArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId] += 1
            #qSA = qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId]
            #qArray[playerPosition[0]][playerPosition[1]][timeSlot][actionId] += self.GetReward2(nextPosition, timeSlot + 1) + int(self.gamma * (maxNextQ - qSA))
            if self.map.HasEnemyAt(nextPosition, timeSlot + 1):
                break
            elif nextPosition == (self.height - 1, self.width - 1): # PlayerDie
                break
            playerPosition = nextPosition

    def RandomAction(self, position, timeSlot):
        temp = [self.CanMove(position, id, timeSlot) for id in range(self.dataHolder.actionIdSize)]
        action = [(x[1], x[2]) for x in temp if x[0]]
        randIdx = random.randrange(len(action))
        return action[randIdx]

    def RandomActionGreedy(self, position, qArray, timeSlot, round, maxRound):
        temp = [self.CanMove(position, id, timeSlot) for id in range(self.dataHolder.actionIdSize)]
        possibleAction = [(x[1], x[2]) for x in temp if x[0]]
        ex = [math.exp(qArray[action[1][0]][action[1][1]][timeSlot][action[0]] / ((maxRound - round)) / 10000) for action in possibleAction]
        sumEx = sum(ex)
        rand = random.uniform(0, sumEx)
        sumX = 0
        for i in range(len(possibleAction)):
            sumX += ex[i]
            if rand < sumX:
                return  possibleAction[i]
        return  possibleAction[len(possibleAction) - 1]

    def RandomActionSimpleGreedy(self, position, qArray, timeSlot, round, maxRound):
        temp = [self.CanMove(position, id, timeSlot) for id in range(self.dataHolder.actionIdSize)]
        possibleAction = sorted([(x[1], x[2]) for x in temp if x[0]])
        posList = []
        for i in range(len(possibleAction)):
            for j in range(i + 1):
                for k in range(j):
                    posList.append(possibleAction[i])

        rand = random.randrange(len(posList))
        return posList[rand]

    def RandomActionGreedy2(self, position, timeSlot):
        temp = [self.CanMove(position, id, timeSlot) for id in range(self.dataHolder.actionIdSize)]
        possibleActions = [(x[1], x[2]) for x in temp if x[0]]

        qArray = self.dataHolder.GetQArray()
        best = max(qArray[pos[0]][pos[1]][timeSlot][aID] for (aID, pos) in possibleActions)
        bestActions = [(aID, pos) for (aID, pos) in possibleActions if qArray[pos[0]][pos[1]][timeSlot][aID] == best]
        otherActions = [(aID, pos) for (aID, pos) in possibleActions if qArray[pos[0]][pos[1]][timeSlot][aID] < best]
        # if (not self.dataHolder.hasReach and random.random() < 0.4) or (self.dataHolder.hasReach and random.random() < 0.75):
        #     freqArray = self.dataHolder.GetFreqArray()
        #     best = min(freqArray[pos[0]][pos[1]][timeSlot][aID] for (aID, pos) in possibleActions)
        #     bestActions = [(aID, pos) for (aID, pos) in possibleActions if freqArray[pos[0]][pos[1]][timeSlot][aID] == best]
        #     otherActions = [(aID, pos) for (aID, pos) in possibleActions if freqArray[pos[0]][pos[1]][timeSlot][aID] > best]
        freqArray = self.dataHolder.GetFreqArray()
        bestF = min(freqArray[pos[0]][pos[1]][timeSlot][aID] for (aID, pos) in possibleActions)
        bestActionsF = [(aID, pos) for (aID, pos) in possibleActions if freqArray[pos[0]][pos[1]][timeSlot][aID] == bestF]
        otherActionsF = [(aID, pos) for (aID, pos) in possibleActions if freqArray[pos[0]][pos[1]][timeSlot][aID] > bestF]

        bestActions += bestActionsF
        otherActions += otherActionsF

        actions = bestActions if (random.random() < 0.8 and len(bestActions) > 0) or len(otherActions) == 0 else otherActions
        randIdx = random.randrange(len(actions))
        return actions[randIdx]

    def CanMove(self, position, actionId, timeSlot):
        dir = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
        x, y = (position[0] + dir[actionId][0]),(position[1] + dir[actionId][1])
        enemies = self.map.GetEnemyAt((x,y), timeSlot)
        crossEnemies = [enemy for enemy in enemies if enemy.GetPositionAt(timeSlot + 1) == position]
        return (0 <= x < self.map.height) and (0 <= y < self.map.width) and len(crossEnemies) == 0, actionId, (x, y)

    def GetReward(self, position, timeSlot):
        if (self.map.HasEnemyAt(position, timeSlot)): # map.HasEnemyAt(timeSlot)
            return -10000000
        elif (position[0] == self.height - 1 and position[1] == self.width - 1):
            return 2000000000
        else:
            return  -timeSlot * ( (self.height - position[0]) + (self.width - position[1]))

    def GetReward2(self, position, timeSlot):
        if (self.map.HasEnemyAt(position, timeSlot)):  # map.HasEnemyAt(timeSlot)
            return -100000
        elif (position[0] == self.height - 1 and position[1] == self.width - 1):
            return 200000
        else:
            return ((position[0] + position[1]) * 2 - timeSlot) * 10

    def GetPathFromQ(self):

        qArray = self.dataHolder.GetQArray()
        paths = []
        position = (0, 0)
        paths.append(position)
        for timeSlot in range(self.dataHolder.maxTimeSlot):
            temp = [self.CanMove(position, id, timeSlot) for id in range(self.dataHolder.actionIdSize)]
            possibleActions = [(x[1], x[2]) for x in temp if x[0]]
            best = max(qArray[position[0]][position[1]][timeSlot][aID] for (aID, pos) in possibleActions)
            bestActions = [(aID, pos) for (aID, pos) in possibleActions if qArray[position[0]][position[1]][timeSlot][aID] == best]
            randIdx = random.randrange(len(bestActions))
            oldPosition = position
            position = bestActions[randIdx][1]
            paths.append(position)
            if self.map.HasEnemyAt(position, timeSlot + 1):  # map.HasEnemyAt(timeSlot)
                break
            elif  position == (self.height - 1, self.width - 1):
                break
        return paths
