from base.vector import Vector2D


class Movement():
    def __init__(self, human):
        self.human = human
        self.__destination = self.human.rect.center
        self.trueX = self.human.rect.center[0]
        self.trueY = self.human.rect.center[1]

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
        # TODO: get route somehow
        return [(500, 400), (400, 500), (300, 300)]


    def add_move(self, destination):
        """
        Add a movement to current path
        
        :param source: 
        :param destination: 
        :return: 
        """
        if len(self.__route) == 0:
            self.set_destination(destination)
        else:
            self.__route = self.__route + self.calculate_route(source=self.__final_destination, destination=destination)
            self.__final_destination = destination


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
        # print(t_dist, speed)
        if t_dist <= (speed):
            return True