import pygame

pygame.init()

SCREENW = 1025
SCREENH = 513
HH = SCREENH/2
HW = SCREENW/2

MAPW = 65
MAPH = 65

SCREEN = pygame.display.set_mode((SCREENW,SCREENH))

FPS = 60

CLOCK = pygame.time.Clock()
