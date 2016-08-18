from german.gun.basic import BasicGun
from soldier import Soldier
import pygame, math

class Vector2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError("This "+str(key)+" key is not a vector key!")

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            # Vector multiplication
            return self.x * other.x + self.y * other.y
        else:
            # Scalar multiplication
            return Vector2D(self.x * other, self.y * other)

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    def get_angle(self, other, radians=False):
        """Will return the angle between this vector and the other vector."""
        if self.get_length() == 0 or other.get_length() == 0:
            return 0
        if not radians:
            return (360 / (2 * math.pi)) * (math.atan2(other.y, other.x) - math.atan2(self.y, self.x))
        else:
            return math.atan2(other.y, other.x) - math.atan2(self.y, self.x)

    def normalize(self): # divides a vector by its length
        l = self.length()
        if l != 0:
            return (self.x / l, self.y / l)
        return None

    def length(self): # get length (used for normalize)
        return math.sqrt((self.x**2 + self.y**2))

class GermanSoldier(Soldier):

    def __init__(self):
        self.speed = 2
        img = pygame.image.load('uparrow.png')
        img = pygame.transform.smoothscale(img, (50, 50))
        super(GermanSoldier, self).__init__(img, BasicGun())
        self.destination = self.rect.center
        self.trueX = self.rect.center[0]  # created because self.rect.center does not hold
        self.trueY = self.rect.center[1]  # decimal values but these do

    def update(self):
        self.rotate()
        self.move()

    def moveTo(self, destination):
        self.destination = destination
        # Create a vector pointing at the mouse position.
        mouse_pos = Vector2D(*self.destination)

        # Create a vector pointing from the image towards the mouse position.
        rel_mouse_pos = mouse_pos - Vector2D(self.rect.center[0], self.rect.center[1])

        # Calcuate the angle between the y_axis and the vector pointing from the image towards the mouse position.
        y_axis = Vector2D(0, -1)
        self.angle = math.radians(- y_axis.get_angle(rel_mouse_pos))

    def move(self):
        self.dir = self.get_direction(self.destination)  # get direction
        if self.dir:  # if there is a direction to move

            if self.distance_check(self.dist):  # if we need to stop
                self.rect.center = self.destination  # center the sprite on the target

            else:  # if we need to move normal
                self.trueX += (self.dir[0] * self.speed)  # calculate speed from direction to move and speed constant
                self.trueY += (self.dir[1] * self.speed)
                self.rect.center = (round(self.trueX), round(self.trueY))  # apply values to sprite.center

    def get_direction(self, target):
        if target:  # if the square has a target
            position = Vector2D(self.rect.centerx, self.rect.centery)  # create a vector from center x,y value
            target = Vector2D(target[0], target[1])  # and one from the target x,y
            self.dist = target - position  # get total distance between target and position

            direction = self.dist.normalize()  # normalize so its constant in all directions
            return direction

    def distance_check(self, dist):
        dist_x = dist[0] ** 2  # gets absolute value of the x distance
        dist_y = dist[1] ** 2  # gets absolute value of the y distance
        t_dist = dist_x + dist_y  # gets total absolute value distance
        speed = self.speed ** 2  # gets aboslute value of the speed
        print(t_dist, speed)
        if t_dist < (speed):  # read function description above
            return True

    def rotate(self):
        # """Updates the player's orientation."""

        # Create a vector pointing at the mouse position.
        mouse_pos = Vector2D(*pygame.mouse.get_pos())

        # Create a vector pointing from the image towards the mouse position.
        rel_mouse_pos = mouse_pos - Vector2D(self.get_current_location()[0], self.get_current_location()[1])

        # Calcuate the angle between the y_axis and the vector pointing from the image towards the mouse position.
        y_axis = Vector2D(0, -1)
        angle = -y_axis.get_angle(rel_mouse_pos)  # Negating because pygame rotates counter-clockwise.

        # Create the rotated copy.
        self.image = pygame.transform.rotate(self.original, angle)

        # Make sure your rect represent the actual Surface.
        self.rect = self.image.get_rect()

        # Since the dimension probably changed you should move its center back to where it was.
        self.rect.center = self.get_current_location()[0], self.get_current_location()[1]