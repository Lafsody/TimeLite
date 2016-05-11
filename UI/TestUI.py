import sys, pygame, math
from UI import Buttons

pygame.init()

pygame.display.set_caption("TimeLite.py")

width, height = 0, 0
underBarSize = 100
screen = None

color = {}
color['black'] = 0, 0, 0
color['white'] = 255, 255, 255
color['gray'] = 180, 180, 180
color['green'] = 120, 255, 124
color['red'] = 255, 125, 125

playerObj = None
enemyObjList = []
LearnButton = Buttons.Button()
RerunButton = Buttons.Button()

def Init(w, h, enemiesNo):
    global width, height, screen
    width, height = w, h
    screen = pygame.display.set_mode((w * 80, h * 80 + underBarSize))

    global playerObj, enemyObjList
    playerPic = pygame.image.load("player.png")
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
            if i == 0 and j == 0: pygame.draw.rect(screen, color['green'], (i * 80, j * 80, 80, 80))
            if i == width-1 and j == height-1: pygame.draw.rect(screen, color['red'], (i * 80, j * 80, 80, 80))
            pygame.draw.rect(screen, color['white'], (i * 80, j * 80, 80, 80), 2)
    basicFont = pygame.font.SysFont(None, 34)
    textStart = basicFont.render('START', True, color["white"], color["green"])
    textGoal = basicFont.render('GOAL!', True, color["white"], color["red"])
    textStartRect = textStart.get_rect()
    textGoalRect = textGoal.get_rect()
    textStartRect.centerx = screen.get_rect().x + 40
    textStartRect.centery = screen.get_rect().y + 40
    textGoalRect.centerx = screen.get_rect().x + width*80 - 40
    textGoalRect.centery = screen.get_rect().y + height*80 - 40
    screen.blit(textStart, textStartRect)
    screen.blit(textGoal, textGoalRect)

from time import sleep
def Update(pPos, ePosList, roundPerTimeSlot, tpf):
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
        for t in range(roundPerTimeSlot):
            dist = 80 / roundPerTimeSlot
            sleep(tpf)
            FillBG()
            playerPos.move_ip(tuple(x for x in  (dist * (pPos[0] - oldPlayerPos[0]), dist * (pPos[1] - oldPlayerPos[1]))))
            for i in range(len(enemyPosList)):
                enemyPosList[i].move_ip(tuple(x for x in (dist * (ePosList[i][0] - oldEnemyPosList[i][0]),dist * (ePosList[i][1] - oldEnemyPosList[i][1]))))
            screen.blit(playerObj, playerPos)
            for i in range(len(enemyPosList)):
                screen.blit(enemyObjList[i], enemyPosList[i])

            # Parameters:        surface,      color,     x,   y, length, height, width,  text, text_color
            LearnButton.create_button(screen, (125, 125, 255), width * 80 - underBarSize, height * 80, underBarSize, underBarSize, 0, "Learn+", (255, 255, 255))
            RerunButton.create_button(screen, (255, 125, 255), width * 80 - underBarSize * 2, height * 80, underBarSize,
                                  underBarSize, 0, "Rerun", (255, 255, 255))
            pygame.display.flip()
    oldPlayerPos = pPos
    oldEnemyPosList = [ePos for ePos in ePosList]



