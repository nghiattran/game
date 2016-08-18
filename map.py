from copy import deepcopy
import asyncio
from algo.astar import AStar
from base.vector import Vector2D
from multiprocessing import Pool

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Map(metaclass=Singleton):
    __map = []
    __mapString = ''
    __instance = None
    def __init__(self):

        for x in range(0, 80):
            self.__map.append([])
            for y in range(0, 60):
                self.__map[x].append(0)

        for x in range(40, 45):
            for y in range(0, 50):
                self.__map[x][y] = 1

    def __str__(self, map=None):
        if map is None:
            map = self.__map

        return self.to_string(map)

    def to_string(self, map):
        rows = []
        for index, val in enumerate(map):
            rows.append(''.join(str(v) for v in map[index]))

        return '\n'.join(rows)

    def get_map(self):
        return self.__map

    def clone_map(self):
        return deepcopy(self.__map)

    def find_path(self, source, destination):
        map = self.clone_map()
        map[int(source[0] / 10)][int(source[1] / 10)] = 'S'
        map[int(destination[0] / 10)][int(destination[1] / 10)] = 'T'
        map = self.to_string(map)

        a = AStar(map)
        for i in a.step():
            pass

        if len(a.path) == 0:
            return []

        return self.shorten(a.path)

    def shorten(self, path):
        for x, valx in enumerate(path):
            path[x] = (path[x][1] * 10, path[x][0] * 10)

        realpath = [path[0]]
        old_vector = None
        for index in range(1, len(path)):
            vector = Vector2D(path[index][0] - path[index - 1][0],
                              path[index][1] - path[index - 1][1])

            if old_vector is None:
                old_vector = vector
                realpath.append(path[index])
                continue
            else:
                if old_vector == vector:
                    realpath.pop()
                else:
                    old_vector = vector
                realpath.append(path[index])
        return realpath

    def cmp(self, tlp1, tlp2):
        if len(tlp1) == len(tlp2):
            for x in range(0, len(tlp1)):
                if tlp1[x] != tlp2[x]:
                    return False
            return True
        return False
