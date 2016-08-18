from human import Human
import pygame, math


class Soldier (Human):
    __gun = None

    def __init__(self, img, gun):
        super().__init__(image=img)
        self.__img = img
        self.__gun = gun

    def fire(self, destination):
        self.__gun.shoot(destination)

    def get_gun(self):
        return self.__gun