import pygame
from base.movement import Movement
from map import Map


class Human(pygame.sprite.Sprite):
    radius = 25

    def __init__(self, location, image = None, speed=1):
        super().__init__()
        self.__speed = speed
        self.set_img(image)
        self.rect = self.image.get_rect()
        self.location = location
        self.rect.center = location
        self.movement = Movement(self)

    def update(self):
        pass

    def set_img(self, img):
        self.image = img
        self.original = img

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def add_move(self, destination):
        self.movement.add_move(destination=destination)

    def highlight_path(self, screen):
        self.movement.highlight(screen=screen)