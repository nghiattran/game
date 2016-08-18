import pygame, math, time
from german.soldier import GermanSoldier

pygame.init()
red = (255, 64, 64)
BLUE  = (  0,   0, 255)
screen = gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Static')
clock = pygame.time.Clock()

crashed = False
player = GermanSoldier((500, 500))
ai = GermanSoldier((100, 100))

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

player.moveTo((500,500))
point = player.rect.center
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONUP and pygame.key.get_mods() & pygame.KMOD_SHIFT:
            pos = pygame.mouse.get_pos()
            player.add_move(pos)

        # if event.type == pygame.MOUSEBUTTONUP:
        #     pos = pygame.mouse.get_pos()
        #     player.moveTo(pos)



    gameDisplay.fill((red))

    all_sprites_list.update()

    pygame.display.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
quit()
