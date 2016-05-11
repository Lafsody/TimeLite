from Game import Enemy

class Map:
    def __init__(self, height = 0, width = 0, enemies = []):
        self.height = height
        self.width = width
        self.enemies = enemies

    def HasEnemyAt(self, position, timeSlot):
        for enemy in self.enemies:
            if enemy.GetPositionAt(timeSlot) == position:
                return True
        return False

    def GetEnemyAt(self, position, timeSlot):
        return [enemy for enemy in self.enemies if enemy.GetPositionAt(timeSlot) == position]