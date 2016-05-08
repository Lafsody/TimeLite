from State import State

class MenuState(State.State):
    def __init__(self, dataHolder):
        self.dataHolder = dataHolder

    def Init(self):
        print("MenuState")

    def Update(self):
        pass