import math
import pygame

from algo.astar import AStar
from base.vector import Vector2D
from map import Map


class Movement():
    def __init__(self, human):
        self.human = human
        self.__destination = self.human.rect.center
        self.trueX = self.human.rect.center[0]
        self.trueY = self.human.rect.center[1]
        self.__route = []

    def set_destination(self, destination):
        """
        Stop current movements and set another one
        
        :param destination: 
        :return: 
        """
        self.__final_destination = destination
        self.__route = self.calculate_route(self.human.rect.center, destination)
        self.move_sequence()

    def get_destination(self):
        return self.__destination

    def calculate_route(self, source, destination):
        map_obj = Map()
        return map_obj.find_path(source, destination=destination)


    def add_move(self, destination):
        """
        Add a movement to current path
        
        :param source: 
        :param destination: 
        :return: 
        """
        if self.is_stand_still():
            self.set_destination(destination)
        else:
            self.__route = self.__route + self.calculate_route(source=self.__final_destination, destination=destination)
            self.__final_destination = destination

    def is_stand_still(self):
        """
        Check if object is not moving and has to planned moved
        :return:
        """
        return len(self.__route) == 0 and self.__destination == self.human.rect.center

    def get_route(self):
        """
        Get route to the current destination
        
        :return: 
        """
        return self.__route

    def next_move(self):
        """
        Get the next move to get to the destination
        :return: 
        """
        if len(self.__route) > 0:
            return self.__route.pop(0)

    def move_sequence(self):
        if len(self.__route) > 0:
            self.__destination = self.__route.pop(0)

    def move(self):
        """
        Move the object to destination
        :return:
        """
        # hotfix
        if self.__destination == self.human.rect.center:
            self.move_sequence()

        self.dir = self.get_direction(self.__destination)  # get direction
        if self.dir:
            if self.is_stop():  # if we need to stop
                self.human.rect.center = self.__destination
                self.move_sequence()
            else:  # if we need to move normal
                self.trueX += (self.dir[0] * self.human.get_speed())
                self.trueY += (self.dir[1] * self.human.get_speed())
                self.human.rect.center = (round(self.trueX), round(self.trueY))

    def get_direction(self, target):
        if target:  # if the object has a target
            position = Vector2D(self.human.rect.centerx, self.human.rect.centery)
            target = Vector2D(target[0], target[1])
            self.dist = target - position
            direction = self.dist.normalize()
            return direction

    # Stop when either it reach destination or blocked
    def is_stop(self):
        return self.distance_check(self.dist)

    def distance_check(self, dist):
        dist_x = dist[0] ** 2
        dist_y = dist[1] ** 2
        t_dist = dist_x + dist_y
        speed = self.human.get_speed() ** 2

        if t_dist <= (speed):
            return True

    def highlight(self, screen):
        BLUE = (0, 0, 255)
        points = [self.human.rect.center, self.__destination] + self.__route

        for index, val in enumerate(points):
            if index >= 1:
                # pygame.draw.line(screen, BLUE, points[index-1], val, 4)
                self.draw_dashed_line(surf=screen, color=BLUE, start_pos=points[index-1], end_pos=val)

    def draw_dashed_line(self, surf, color, start_pos, end_pos, width=1, dash_length=10):
        origin = Vector2D(start_pos[0], start_pos[1])
        target = Vector2D(end_pos[0], end_pos[1])
        displacement = target - origin
        length = len(displacement)
        if length == 0:
            return
        slope = displacement.div(length)

        for index in range(0, int(length / dash_length), 2):
            start = origin + (slope * index * dash_length)
            end = origin + (slope * (index + 1) * dash_length)
            pygame.draw.line(surf, color, start.get(), end.get(), width)

    # def find_path(self, destination):
    #     map_obj = self.human.get_map()
    #     return map_obj.find_path(self.human.rect.center, destination=destination)