import pygame, math, time

from algo.astar import AStar
from base.vector import Vector2D
from german.soldier import GermanSoldier
from map import Map

pygame.init()
red = (255, 64, 64)
BLUE  = (  0,   0, 255)
screen = gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Static')
clock = pygame.time.Clock()

crashed = False
map = Map()
player = GermanSoldier((50, 50))
ai = GermanSoldier((100, 100))

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

point = player.rect.center

while not crashed:
    gameDisplay.fill((red))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONUP and pygame.key.get_mods() & pygame.KMOD_SHIFT:
            pos = pygame.mouse.get_pos()
            player.add_move(pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            player.moveTo(pos)

    player.highlight_path(screen=screen)

    all_sprites_list.update()
    pygame.draw.rect(screen, BLUE, (400, 0, 50, 500), 4)
    pygame.display.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(50)



pygame.quit()
quit()

