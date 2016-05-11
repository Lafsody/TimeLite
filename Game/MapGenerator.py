from Game import Map
from Game import Enemy
import random

def Generate(height = 10, width = 10, numEnemy = 10):
    enemies = GenerateEnemies(numEnemy, height, width)
    map = Map.Map(height, width, enemies)
    return map

def GenerateEnemies(numEnemy = 0, height = 1, width = 1):
    enemies = []
    for i in range(numEnemy):
        enemy = GenerateEnemy(height, width)
        enemies.append(enemy)
    return enemies

def GenerateEnemy(height, width):
    start = (0, 0)
    while (start == (0, 0) or start == (height - 1, width - 1)) :
        start = (random.randrange(height), random.randrange(width))

    direction = random.randint(0, 1)
    target = (height - 1, width - 1)
    while (target == (height - 1, width - 1)):
        target = (start[0], random.randrange(width)) if direction else (random.randrange(height), start[1])

    #print("Dir: %d, FROM: %s TO %s" % (direction, start, target))
    return Enemy.Enemy(start, target)

#map = Generate(10, 20, 2)

#for t in range(20):
#    print("T = %d" % t)
#    for enemy in map.enemies:
#        print(enemy.GetPositionAt(t))
