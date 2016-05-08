from Game import Enemy

class Map:
    def __init__(self, height = 0, width = 0, enemies = []):
        self.height = height
        self.width = width
        self.enemies = enemies