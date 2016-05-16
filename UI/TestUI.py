import sys, pygame, math
from UI import Buttons
from UI import  SliderBar

pygame.init()

pygame.display.set_caption("TimeLite.py")

width, height = 0, 0
underBarHeigth = 50
underBarWidth = 200
# Slider Bar
barSize = 0 #20
borderTop = 0 #3
borderSide = 3
underOverallSize = underBarHeigth + barSize + 2 * borderTop

screen = None

color = {}
color['black'] = 0, 0, 0
color['white'] = 255, 255, 255
color['gray'] = 180, 180, 180
color['green'] = 120, 255, 124
color['red'] = 255, 125, 125
color['blue'] = 125, 125, 255

playerObj = None
enemyObjList = []
ReGenerateButton = Buttons.Button()
LearnButton = Buttons.Button()
RerunButton = Buttons.Button()
timeline = SliderBar.SliderBar()

def Init(w, h, enemiesNo):
    global width, height, screen
    width, height = w, h
    screen = pygame.display.set_mode((w * 80, h * 80 + underOverallSize))

    global playerObj, enemyObjList
    playerPic = pygame.image.load("player.png")
    playerObj = pygame.transform.scale(playerPic, (80, 80))
    enemyPic = pygame.image.load("enemy.png")
    enemyObjList = [pygame.transform.scale(enemyPic, (80, 80)) for i in range(enemiesNo)]

    global underBarWidth
    underBarWidth = (w * 80) / 3

    timeline.setValue(borderSide, height * 80 + borderTop, width * 80 - borderSide * 2, barSize)

oldPlayerPos = None
oldEnemyPosList = None
oldKnobX = None

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
def Update(pPos, ePosList, knobX, roundPerTimeSlot, tpf):
    global width, height, screen, color, playerObj, enemyObjList
    global playerPos, enemyPosList, oldPlayerPos, oldEnemyPosList, oldKnobX

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
            trackDist = 5 / roundPerTimeSlot
            sleep(tpf)
            FillBG()
            playerPos.move_ip(tuple(x for x in  (dist * (pPos[0] - oldPlayerPos[0]), dist * (pPos[1] - oldPlayerPos[1]))))
            for i in range(len(enemyPosList)):
                enemyPosList[i].move_ip(tuple(x for x in (dist * (ePosList[i][0] - oldEnemyPosList[i][0]),dist * (ePosList[i][1] - oldEnemyPosList[i][1]))))
            screen.blit(playerObj, playerPos)
            for i in range(len(enemyPosList)):
                screen.blit(enemyObjList[i], enemyPosList[i])

            #Draw Button
            # Parameters:        surface,      color,     x,   y, length, height, width,  text, text_color
            ReGenerateButton.create_button(screen, (125, 125, 255), 0,
                                      height * 80 + barSize + 2 * borderTop, underBarWidth, underBarHeigth, 0, "ReGenerate",
                                      (255, 255, 255))
            LearnButton.create_button(screen, (125, 125, 255), width * 80 - underBarWidth, height * 80 + barSize + 2 * borderTop, underBarWidth, underBarHeigth, 0, "Learn+", (255, 255, 255))
            RerunButton.create_button(screen, (125, 125, 255), width * 80 - underBarWidth * 2, height * 80 + barSize + 2 * borderTop, underBarWidth,
                                  underBarHeigth, 0, "Rerun", (255, 255, 255))
            #Draw Slider Bar
            # screen.blit(screen, ((timeline.knob.left * timeline.maxTimeSlot) * -1, 0))
            # if t % 4 == 0:
            #     timeline.knob.x += trackDist * (knobX[0] - oldKnobX[0])
            # timeline.draw_sliderBar(screen, color["white"], color["blue"], color["red"])

            pygame.display.flip()

    timeline.knob.x = knobX[0]
    oldPlayerPos = pPos
    oldEnemyPosList = [ePos for ePos in ePosList]
    oldKnobX = knobX



