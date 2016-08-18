from base.human import Human


class Soldier (Human):
    __gun = None

    def __init__(self, img, gun, location, speed=2):
        super().__init__(image=img, location=location, speed=speed)
        self.__img = img
        self.__gun = gun

    def fire(self, destination):
        self.__gun.shoot(destination)

    def get_gun(self):
        return self.__gun