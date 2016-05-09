import sys, pygame, math

pygame.init()
width, height = 0, 0
screen = None

color = {}
color['black'] = 0, 0, 0
color['white'] = 255, 255, 255
color['gray'] = 180, 180, 180

playerObj = None
enemyObjList = []

def Init(w, h, enemiesNo):
    global width, height, screen
    width, height = w, h
    screen = pygame.display.set_mode((w * 80, h * 80))

    global playerObj, enemyObjList
    playerPic = pygame.image.load("ball.gif")
    playerObj = pygame.transform.scale(playerPic, (80, 80))
    enemyPic = pygame.image.load("enemy.png")
    enemyObjList = [pygame.transform.scale(enemyPic, (80, 80)) for i in range(enemiesNo)]


def Update(pPos, ePosList):
    global width, height, screen, color, playerObj, enemyObjList
    screen.fill(color['gray'])
    mRC = [[pygame.draw.rect(screen, color['white'], (i * 80, j * 80, 80, 80), 2) for i in range(width)] for j in range(height)]

    screen.blit(playerObj, mRC[pPos[0]][pPos[1]])
    for i in range(len(ePosList)):
        screen.blit(enemyObjList[i], mRC[ePosList[i][0]][ePosList[i][1]])

    pygame.display.flip()


