import sys, pygame


def init(width, height):
    pygame.init()

    # enter window size here, width, height is multiple of 80
    size = width, height
    color = {}
    color['black'] = 0, 0, 0
    color['white'] = 255, 255, 255
    color['gray'] = 180, 180, 180

    playerpos = [0, 0]

    w, h = (int)(width/80), (int)(height/80)
    mrc = [[" " for x in range(w)] for y in range(h)]

    screen = pygame.display.set_mode(size)
    ball = pygame.image.load("ball.gif")
    ball2 = pygame.transform.scale(ball, (80, 80))
    ball3 = pygame.transform.scale(ball, (80, 80))
    ballrect3 = ball3.get_rect()

    pygame.key.set_repeat(1, 150)
    while 1:

        screen.fill(color['gray'])
        for i in range(w):
            for j in range(h):
                mrc[j][i] = pygame.draw.rect(screen, color['white'], (i * 80, j * 80, 80, 80), 2)
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
                move(ball3, playerpos, "left", w, h, color, mrc, screen)
            if keystate[pygame.K_RIGHT]:
                move(ball3, playerpos, "right", w, h, color, mrc, screen)
            if keystate[pygame.K_UP]:
                move(ball3, playerpos, "up", w, h, color, mrc, screen)
            if keystate[pygame.K_DOWN]:
                move(ball3, playerpos, "down", w, h, color, mrc, screen)

        pygame.display.flip()
    return


def filltable(w, h, color, mrc, screen):
    for i in range(w):
        for j in range(h):
            mrc[j][i] = pygame.draw.rect(screen, color['white'], (i * 80, j * 80, 80, 80), 2)

def move(obj,playerpos, dir, w, h, color, mrc, screen):
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
    elif playerpos[0] > h-1:
        playerpos[0] = h-1
    elif playerpos[1] < 0:
        playerpos[1] = 0
    elif playerpos[1] > w-1:
        playerpos[1] = w-1
    else:
        for i in range(1,40):
            screen.fill(color['gray'])
            filltable(w, h, color, mrc, screen)
            balltemp = balltemp.move(spd)
            screen.blit(obj, balltemp)
            pygame.display.update()
    screen.blit(obj, mrc[playerpos[0]][playerpos[1]])
    pygame.display.flip()
    return;

# enter window size here, width, height is multiple of 80
init(640, 480)