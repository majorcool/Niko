import random

import pygame
from settings import *
from scene import *
from obstacle import *
from dinosaur import *
import sys

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()

ground = Ground(pygame.image.load(IMAGE_PATHS.get("ground")), (0,200))
din = Dinosaur(D_IMG, 0.2 * SCREENSIZE[0], GROUND_LVL)
ptes = []
cacs = []

#scr = Scoreboard(S_IMG, (0,0))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                din.jump()
            elif event.key == pygame.K_DOWN:
                din.duck()
            else:
                din.stand() # anything other than duck and jump key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                din.stand() #K_DOWN relesed


    for i in ptes:
        if pygame.sprite.collide_mask(din, i):
            din.die()
            din.update()

    for i in cacs:
        if pygame.sprite.collide_mask(din, i):
            din.die()
            din.update()

    screen.fill(BACKGROUND_COLOR)

    ground.update()
    ground.draw(screen)
   # scr.update()
    #scr.draw(screen)

    if random.randint(0,300) == 0: # about once every 300 frames
        ptes.append(Pterodactyl(P_IMG, (SCREENSIZE[0], random.randint(PTES_BOTTOM, PTES_TOP))))
    for i in ptes:
        i.update()
        i.draw(screen)
    if random.randint(0,100) == 0:
        cacs.append(Cactus(C_IMG, (SCREENSIZE[0], GROUND_LVL), random.randint(0, 5)))
    for i in cacs:
        i.update()
        i.draw(screen)
    din.update()
    din.draw(screen)

    #scr.score = ground.displacement // 50
    pygame.display.update()
    clock.tick(FPS)
