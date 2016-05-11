import sys, pygame, math


def init(width, height, player, enemy):
    pygame.init()

    # enter window size here, width, height is multiple of 80
    size = width, height
    color = {}
    color['black'] = 0, 0, 0
    color['white'] = 255, 255, 255
    color['gray'] = 180, 180, 180

    w, h = (int)(width/80), (int)(height/80)
    mrc = [[" " for x in range(w)] for y in range(h)]

    playerpos = [0, 0]
    enemypos = [[h-1,w-1] for i in range(len(enemy))]
    print(enemypos)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Timelite')

    ball = pygame.image.load("ball.gif")
    ball2 = pygame.transform.scale(ball, (80, 80))
    ball3 = pygame.transform.scale(ball, (80, 80))
    ballrect3 = ball3.get_rect()

    # enemypic = pygame.image.load("enemy.png")
    # enemypic2 = pygame.transform.scale(enemypic, (80,80))
    enemylist = [pygame.transform.scale(pygame.image.load("enemy.png"),(80,80)) for i in range(len(enemy))]
    # for i in range(len(enemy)):
    #     enemylist.append(pygame.transform.scale(pygame.image.load("enemy.png"),(80,80)))
    # print(enemylist)


    pygame.key.set_repeat(1, 150)

    while 1:

        screen.fill(color['gray'])
        for i in range(w):
            for j in range(h):
                mrc[j][i] = pygame.draw.rect(screen, color['white'], (i * 80, j * 80, 80, 80), 2)

        # font = pygame.font.Font(None, 12)
        # text = font.render("Start", 1, (10, 10, 10))
        # textpos = text.get_rect()
        # textpos.centerx = mrc[0][0].get_rect().centerx
        # mrc[0][0].blit(text, textpos)

        basicFont = pygame.font.SysFont(None, 12)
        text = basicFont.render('Hello world!', True, color["white"], color["gray"])
        textRect = text.get_rect()
        textRect.centerx = mrc[0][0].centerx
        textRect.centery = mrc[0][0].centery
        screen.blit(text, textRect)

        screen.blit(ball3, mrc[playerpos[0]][playerpos[1]])
        # screen.blit(enemypic2, mrc[3][3])

        # print(player)
        # print(playerpos)
        playerdirnum = [player[0] - playerpos[0], player[1] - playerpos[1]]
        # print(playerdirnum)
        dir = ""
        if playerdirnum[0] == 0 and playerdirnum[1] == 1:
            dir = "right"
        elif playerdirnum[0] == 0 and playerdirnum[1] == -1:
            dir = "left"
        elif playerdirnum[0] == -1 and playerdirnum[1] == 0:
            dir = "up"
        elif playerdirnum[0] == 1 and playerdirnum[1] == 0:
            dir = "down"

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

        for i in range(len(enemy)):
            # print(mrc[enemypos[i][0]][enemypos[i][1]])
            # print(str(enemypos[i][0]) +" "+ str(enemypos[i][1]))
            screen.blit(enemylist[i], mrc[enemypos[i][0]][enemypos[i][1]])

        enemydirnum = [0,0]
        for i in range(len(enemy)):
            enemydirnum[0] = enemy[i][0] - enemypos[i][0]
            enemydirnum[1] = enemy[i][1] - enemypos[i][1]

            dirx = ""
            if enemydirnum[1] > 0: dirx = "right"
            elif enemydirnum[1] < 0: dirx = "left"
            diry = ""
            if enemydirnum[0] > 0: diry = "down"
            elif enemydirnum[0] < 0: diry = "up"

            print("xdir=" + dirx + " ydir=" +diry)
            print("enemydirnum[0]=" + str(enemydirnum[0]) + " enemydirnum[1]=" + str(enemydirnum[1]))
            for j in range(int(math.fabs(enemydirnum[0]))):
                # move naw norn
                print("aaaaa")
                move(enemylist[i], enemypos[i], dirx, w, h, color, mrc, screen)
            for j in range(int(math.fabs(enemydirnum[1]))):
                # move naw tung
                move(enemylist[i], enemypos[i], diry, w, h, color, mrc, screen)

        move(ball3, playerpos, dir, w, h, color, mrc, screen)

        pygame.display.flip()
    return


def filltable(w, h, color, mrc, screen):
    for i in range(w):
        for j in range(h):
            mrc[j][i] = pygame.draw.rect(screen, color['white'], (i * 80, j * 80, 80, 80), 2)

def move(obj,playerpos, dir, w, h, color, mrc, screen):
    spd = [0,0]
    balltemp = mrc[playerpos[0]][playerpos[1]]
    tmp = [playerpos[0], playerpos[1]]
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
    # else:
    #     for i in range(1,40):
    #         # screen.fill(color['gray'])
    #         # filltable(w, h, color, mrc, screen)
    #         # pygame.draw.rect(screen, color['gray'], (tmp[0] * 80, tmp[1] * 80, 80, 80))
    #         # pygame.draw.rect(screen, color['white'], (tmp[0] * 80, tmp[1] * 80, 80, 80), 2)
    #         # pygame.draw.rect(screen, color['gray'], (playerpos[0] * 80, playerpos[1] * 80, 80, 80))
    #         # pygame.draw.rect(screen, color['white'], (playerpos[0] * 80, playerpos[1] * 80, 80, 80), 2)
    #         balltemp = balltemp.move(spd)
    #         screen.blit(obj, balltemp)
    #         pygame.display.update()
    screen.blit(obj, mrc[playerpos[0]][playerpos[1]])
    return;

# def enemymove(obj,enemypos, dir, w, h, color, mrc, screen):
#     spd = [0,0]
#     enemytmp = mrc[playerpos[0]][playerpos[1]]
#     tmp = [playerpos[0], playerpos[1]]
#     if dir == "left":
#         playerpos[0] += 0
#         playerpos[1] -= 1
#         spd = [-2,0]
#         print("left")
#     elif dir == "right":
#         playerpos[0] += 0
#         playerpos[1] += 1
#         spd = [2, 0]
#         print("right")
#     elif dir == "up":
#         playerpos[0] -= 1
#         playerpos[1] += 0
#         spd = [0, -2]
#         print("up")
#     elif dir == "down":
#         playerpos[0] += 1
#         playerpos[1] += 0
#         spd = [0, 2]
#         print("down")
#     if playerpos[0] < 0:
#         playerpos[0] = 0
#     elif playerpos[0] > h-1:
#         playerpos[0] = h-1
#     elif playerpos[1] < 0:
#         playerpos[1] = 0
#     elif playerpos[1] > w-1:
#         playerpos[1] = w-1
#     else:
#         for i in range(1,40):
#             # screen.fill(color['gray'])
#             # filltable(w, h, color, mrc, screen)
#             pygame.draw.rect(screen, color['gray'], (tmp[0] * 80, tmp[1] * 80, 80, 80))
#             pygame.draw.rect(screen, color['white'], (tmp[0] * 80, tmp[1] * 80, 80, 80), 2)
#             pygame.draw.rect(screen, color['gray'], (playerpos[0] * 80, playerpos[1] * 80, 80, 80))
#             pygame.draw.rect(screen, color['white'], (playerpos[0] * 80, playerpos[1] * 80, 80, 80), 2)
#             balltemp = balltemp.move(spd)
#             screen.blit(obj, balltemp)
#             pygame.display.update()
#     screen.blit(obj, mrc[playerpos[0]][playerpos[1]])
#     return;





# enter window size here, width, height is multiple of 80
player = [1,0]
enemy = [[3,4],[1,2],[3,5],[2,1]]
init(640, 480, player, enemy)