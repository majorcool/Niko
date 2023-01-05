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
din = Dinosaur(D_IMG, 0.2 * SCREENSIZE[0], 200)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_UP):
                print("jmp")
                din.jump()


    screen.fill(BACKGROUND_COLOR)

    ground.update()
    ground.draw(screen)

    din.update()
    din.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
