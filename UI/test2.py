import sys, pygame

def filltable():
    for i in range(w):
        for j in range(h):
            mrc[j][i] = pygame.draw.rect(screen, white, (i * 80, j * 80, 80, 80), 2)

def move(obj,playerpos, dir):
    spd = [0,0]
    balltemp = mrc[playerpos[0]][playerpos[1]]
    if dir == "left":
        playerpos[0] += 0
        playerpos[1] -= 1
        spd = [-2,0]
        print("left")
    elif dir == "right":
        playerpos[0] += 0
        playerpos[1] += 1
        spd = [2, 0]
        print("right")
    elif dir == "up":
        playerpos[0] -= 1
        playerpos[1] += 0
        spd = [0, -2]
        print("up")
    elif dir == "down":
        playerpos[0] += 1
        playerpos[1] += 0
        spd = [0, 2]
        print("down")
    if playerpos[0] < 0:
        playerpos[0] = 0
    elif playerpos[0] > 9:
        playerpos[0] = 9
    elif playerpos[1] < 0:
        playerpos[1] = 0
    elif playerpos[1] > 9:
        playerpos[1] = 9
    else:
        for i in range(1,40):
            screen.fill(gray)
            filltable()
            balltemp = balltemp.move(spd)
            screen.blit(obj, balltemp)
            pygame.display.update()
    screen.blit(obj, mrc[playerpos[0]][playerpos[1]])
    pygame.display.flip()
    return;

pygame.init()

size = width, height = 800, 800
speed = [3, 2]
black = 0, 0, 0
white = 255, 255, 255
gray = 180, 180, 180

playerpos = [0, 0]

w, h = 10, 10
m = [[" " for x in range(w)] for y in range(h)]
mrc = [[" " for x in range(w)] for y in range(h)]

screen = pygame.display.set_mode(size)
ball = pygame.image.load("ball.gif")
ball2 = pygame.transform.scale(ball, (80, 80))
ball3 = pygame.transform.scale(ball, (80, 80))
# ballrect = ball2.get_rect()
ballrect3 = ball3.get_rect()

pygame.key.set_repeat(1, 150)
while 1:
    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(gray)
    for i in range(w):
        for j in range(h):
            mrc[j][i] = pygame.draw.rect(screen, white, (i * 80, j * 80, 80, 80), 2)
    # screen.blit(ball2, ballrect)
    screen.blit(ball3, mrc[playerpos[0]][playerpos[1]])


    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         move(ball3,playerpos, "left")
        #     if event.key == pygame.K_RIGHT:
        #         move(ball3,playerpos,  "right")
        #     if event.key == pygame.K_UP:
        #         move(ball3,playerpos,  "up")
        #     if event.key == pygame.K_DOWN:
        #         move(ball3,playerpos,  "down")
        if keystate[pygame.K_LEFT]:
            move(ball3, playerpos, "left")
        if keystate[pygame.K_RIGHT]:
            move(ball3, playerpos, "right")
        if keystate[pygame.K_UP]:
            move(ball3, playerpos, "up")
        if keystate[pygame.K_DOWN]:
            move(ball3, playerpos, "down")

    pygame.display.flip()



