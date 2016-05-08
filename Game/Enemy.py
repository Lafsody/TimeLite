
class Enemy:
    def __init__(self, startPosition = (0, 0), targetPosition = (0, 0)):
        self.startPosition = startPosition
        self.targetPosition = targetPosition

    def GetPositionAt(self, timeSlot):
        start, target = self.startPosition, self.targetPosition
        if start == target:
            return start

        direction = 1 if start[0] == target[0] else 0
        low, high = (start[1], target[1]) if direction else (start[0], target[0])
        if low > high:
            low, high = high, low
            timeSlot += (high - low)
        interval = (high - low) * 2
        timeSlot %= interval
        position = (interval - timeSlot if timeSlot * 2 >= interval else timeSlot) + low
        return  (start[0], position) if direction else (position, target[1])