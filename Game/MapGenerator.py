from Game import Map
from Game import Enemy

def Generate(width = 10, height = 10, numEnemy = 10):
    enemies = GenerateEnemies(numEnemy, width, height)
    map = Map.Map(width, height, enemies)

def GenerateEnemies(numEnemy = 0, width = 1, height = 1):
    enemies = []
    for i in range(numEnemy):
        enemy = GenerateEnemy(width, height)

def GenerateEnemy(width, height):
    start = (0, 0) #Random It
    target = (0, 0) #RandomIt
    return Enemy.Enemy(start, target)