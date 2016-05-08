
class Enemy:
    def __init__(self, startPosition = (0, 0), targetPosition = (0, 0)):
        self.startPosition = startPosition
        self.targetPosition = targetPosition

    def GetPositionAt(self, timeSlot):
        pass #Fix It
        return  self.startPosition