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
    screen = pygame.display.set_mode((w * 80, h * 80 + 100))

    global playerObj, enemyObjList
    playerPic = pygame.image.load("ball.gif")
    playerObj = pygame.transform.scale(playerPic, (80, 80))
    enemyPic = pygame.image.load("enemy.png")
    enemyObjList = [pygame.transform.scale(enemyPic, (80, 80)) for i in range(enemiesNo)]

oldPlayerPos = None
oldEnemyPosList = None

playerPos = None
enemyPosList = None

def FillBG():
    global color, screen, width, height
    screen.fill(color['gray'])
    for i in range(width):
        for j in range(height):
            pygame.draw.rect(screen, color['white'], (i * 80, j * 80, 80, 80), 2)
from time import sleep
def Update(pPos, ePosList):
    global width, height, screen, color, playerObj, enemyObjList
    global playerPos, enemyPosList, oldPlayerPos, oldEnemyPosList

    pPos = pPos[1], pPos[0]
    ePosList = [(ePos[1], ePos[0]) for ePos in ePosList]

    if playerPos == None:
        FillBG()
        playerPos = pygame.draw.rect(screen, color['white'], (pPos[0] * 80, pPos[1] * 80, 0, 0), 1)
        enemyPosList = [pygame.draw.rect(screen, color['white'], (ePos[0] * 80, ePos[1] * 80, 0, 0), 1) for ePos in ePosList]
        screen.blit(playerObj, playerPos)
        for i in range(len(enemyPosList)):
            screen.blit(enemyObjList[i], enemyPosList[i])
        pygame.display.flip()
    else:
        for t in range(80):
            sleep(0.005)
            FillBG()
            playerPos.move_ip(tuple(x for x in (pPos[0] - oldPlayerPos[0], pPos[1] - oldPlayerPos[1])))
            for i in range(len(enemyPosList)):
                enemyPosList[i].move_ip(tuple(x for x in (ePosList[i][0] - oldEnemyPosList[i][0], ePosList[i][1] - oldEnemyPosList[i][1])))
            screen.blit(playerObj, playerPos)
            for i in range(len(enemyPosList)):
                screen.blit(enemyObjList[i], enemyPosList[i])
            pygame.display.flip()
    oldPlayerPos = pPos
    oldEnemyPosList = [ePos for ePos in ePosList]



