from State import State

class GameState(State.State):
    def __init__(self):
        self.timeSlot = 0

    def Reset(self):
        self.timeSlot = 0

    def Update(self):
        self.timeSlot += 1
        print(self.timeSlot)