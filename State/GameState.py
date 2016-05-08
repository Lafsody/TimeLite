from State import State

class GameState(State.State):
    def __init__(self, dataHolder):
        self.timeSlot = dataHolder.maxTimeSlot
        self.dataHolder = dataHolder

    def Init(self):
        print("GameState")
        self.timeSlot = 0

    def Update(self):
        self.timeSlot += 1