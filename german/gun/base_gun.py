import pygame


class Gun(object):
    name = None
    magazine = None
    in_magazine = None
    amunition = None
    sound = None

    def __init__(self, name, magazine, sound, reload_sound, reload_time, in_magazine = 0, amunition = 0):
        self.name = name
        self.magazine = magazine
        self.sound = pygame.mixer.Sound(sound)
        self.reload_sound = pygame.mixer.Sound(reload_sound)
        self.reload_time = reload_time
        self.amunition = amunition
        self.in_magazine = in_magazine

    def shoot(self, destination):
        if self.in_magazine == 0:
            if self.amunition > 0:
                self.reload()
            else:
                return

        self.in_magazine += -1
        pygame.mixer.init()
        self.sound.play()

    def reload(self):
        if self.magazine > self.amunition:
            self.amunition += -self.magazine
            self.in_magazine = self.magazine
        else:
            self.in_magazine = self.amunition
            self.amunition = 0
