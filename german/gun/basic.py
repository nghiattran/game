import pygame

from german.gun.base_gun import Gun


class BasicGun(Gun):
    def __init__(self):
        super().__init__(name= 'basic', magazine=5, sound='shoot.wav', reload_sound='shoot.wav', reload_time=5,
                         in_magazine= 5, amunition=6)
