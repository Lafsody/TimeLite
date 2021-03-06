
class DataHolder:

    maxTimeSlot = 50
    actionIdSize = 5

    def SetMap(self, targetMap):
        self.map = targetMap
        self.qArray = [[[[0 for l in range(self.actionIdSize)] for k in range(self.maxTimeSlot)] for j in range(self.map.width)] for i in range(self.map.height)]
        self.freqArray = [[[[0 for l in range(self.actionIdSize)] for k in range(self.maxTimeSlot)] for j in range(self.map.width)] for i in range(self.map.height)]
        self.hasReach = False
        self.memorizePath = []
        self.memorizePath.append((0, (0,0)))
        #self.qArray[self.map.height - 1][self.map.width - 1] = [[10000]]
    def GetMap(self):
        return self.map

    def __init__(self):
        self.map = None
        self.qArray = None
        self.freqArray = None

    def SetQArray(self, qArray):
        self.qArray = qArray

    def GetQArray(self):
        return  self.qArray

    def GetFreqArray(self):
        return  self.freqArray