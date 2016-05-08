from Game import Enemy

class Map:
    def __init__(self, width = 0, height = 0, enemies = []):
        self.width = width
        self.height = height
        self.enemies = enemies