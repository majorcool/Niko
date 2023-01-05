import pygame
FPS = 60
TITLE = 'Dino'
BACKGROUND_COLOR = (235, 235, 235)
SCREENSIZE = (700, 300)
IMAGE_PATHS = {
    'ground': 'resources/images/ground/ground.png',
    'cloud': 'resources/images/cloud/cloud.png',
}
D_PATH_header = "resources/images/dinosaur/"
D_IMG = {
    "start" : pygame.image.load(D_PATH_header + "dinosaur-start.png"),
    "jump" : pygame.image.load(D_PATH_header + "dinosaur-jump.png"),
    "run_1" : pygame.image.load(D_PATH_header + "dinosaur-run-1.png"),
    "run_2" : pygame.image.load(D_PATH_header + "dinosaur-run-2.png"),
    "duck_1" : pygame.image.load(D_PATH_header + "dinosaur-duck-1.png"),
    "duck_2" : pygame.image.load(D_PATH_header + "dinosaur-duck-2.png"),
    "die_1" : pygame.image.load(D_PATH_header + "dinosaur-die-1.png"),
    "die_2" : pygame.image.load(D_PATH_header + "dinosaur-die-2.png"),
    "unknown" : pygame.image.load(D_PATH_header + "dinosaur-unknown-1.png"),
}
