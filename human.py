import math, pygame


class Human(pygame.sprite.Sprite):
    __head_angle = 90
    __speed = 5
    location = (100, 100)

    def __init__(self, location = (100, 100), image = None):
        super().__init__()
        self.image = image
        self.original = image
        self.rect = self.image.get_rect()
        self.location = location
        self.rect.center = location

    def get_current_location(self):
        return self.location

    def get_head_angle(self):
        return self.__head_angle

    # def move(self, destination):
    #     if abs(self.location[0] - destination[0]) < 2 and \
    #                     abs(self.location[1] - destination[1]) < 2 :
    #         return self.location
    #
    #     try:
    #         print(destination, self.location)
    #
    #         a = (destination[1] - self.location[1]) / (destination[0] - self.location[0])
    #         angle = math.atan(a)
    #         print(a, math.cos(angle), math.sin(angle))
    #         self.location = ((self.location[0] + self.__speed * math.cos(angle)),
    #                                    (self.location[1] + self.__speed * math.sin(angle)))
    #
    #     finally:
    #         return self.location

    def update(self):
        pass

    def set_img(self, img):
        self.image = img
        self.original = img

