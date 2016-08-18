import pygame, math, time
from german.soldier import GermanSoldier

pygame.init()
red = (255, 64, 64)
BLUE  = (  0,   0, 255)
screen = gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Static')
clock = pygame.time.Clock()

crashed = False
soldier1 = GermanSoldier()
pos = soldier1.get_current_location()

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(soldier1)

point = soldier1.rect.center
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            soldier1.moveTo((500,256))

    gameDisplay.fill((red))

    pygame.draw.line(screen, BLUE, (500,256), soldier1.rect.center, 4)
    pygame.draw.line(screen, BLUE, (500, 256), point, 4)
    all_sprites_list.update()

    pygame.display.update()
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
quit()
