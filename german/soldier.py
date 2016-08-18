import pygame

from base.vector import Vector2D
from german.gun.basic import BasicGun
from soldier import Soldier


class GermanSoldier(Soldier):
    def __init__(self, location):
        img = pygame.image.load('uparrow.png')
        img = pygame.transform.smoothscale(img, (50, 50))
        super(GermanSoldier, self).__init__(img=img, gun=BasicGun(), location=location)

    def update(self):
        # self.rotate()
        self.movement.move()

    def moveTo(self, destination):
        # self.destination = destination
        self.movement.set_destination(destination)

    def rotate(self):
        mouse_pos = Vector2D(*pygame.mouse.get_pos())

        # Create a vector pointing from the image towards the mouse position.
        rel_mouse_pos = mouse_pos - Vector2D(self.location[0], self.location[1])

        # Calcuate the angle between the y_axis and the vector pointing from the image towards the mouse position.
        y_axis = Vector2D(0, -1)
        angle = -y_axis.get_angle(rel_mouse_pos)  # Negating because pygame rotates counter-clockwise.

        # Create the rotated copy.
        self.image = pygame.transform.rotate(self.original_img, angle)

        # Make sure your rect represent the actual Surface.
        self.rect = self.image.get_rect()

        # Since the dimension probably changed you should move its center back to where it was.
        self.rect.center = self.location[0], self.location[1]