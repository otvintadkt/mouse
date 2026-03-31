import random
import maze.Maze
from maze import Maze
from maze.directions import directions
from maze.tiles import Wall_tile
from ui import graphics


class Mouse:
    def __init__(self, x, y, dir=0):
        self.x, self.y = x, y
        self.size = 1 / 20  # доля тайла, тайлы 1x1
        self.speed = 1  # тайлов в секунду
        self.dir = dir
    
    def draw(self):
        graphics.draw_circle("yellow", self.x, self.y, self.size)
    
    def update(self, delta_time):
        # Ничего не умеет вообще
        pass


# немного интеллекта
class Mouse2(Mouse):
    def __init__(self, x, y, dir=0):
        super().__init__(x, y, dir)
        self.x, self.y = x, y
        self.size = 1 / 20  # доля тайла, тайлы 1x1
        self.speed = 1  # тайлов в секунду
        self.dir = 0
        self.new_dir = [1, 0]
    
    def draw(self):
        graphics.draw_circle("yellow", self.x, self.y, self.size)
    
    def update(self, delta_time):
        cur_tile = Maze.get_tile(self.x, self.y)
        dx, dy = directions[self.dir]
        self.x += dx * self.speed * delta_time
        self.y += dy * self.speed * delta_time
        next_tile = cur_tile.get_neighb_tile(self.dir)
        if cur_tile.dist_to_border(self.x, self.y, self.dir) < 0.2 and (
                next_tile is None or isinstance(next_tile, Wall_tile)):
            self.dir = (self.dir + 3) % 4


class SmartMouse(Mouse2):
    def __init__(self, x, y, dir=0):
        super().__init__(x, y, dir)
        self.x, self.y = x, y
        self.size = 1 / 20  # доля тайла, тайлы 1x1
        self.speed = 1  # тайлов в секунду
        self.dir = 0
        self.new_dir = [1, 0]
        self.cheese_x = 1000000000000
        self.cheese_y = 1000000000000
    
    def goto_cheese(self, cheese_x, cheese_y):
        self.cheese_x = cheese_x
        self.cheese_y = cheese_y
    
    def update(self, delta_time):
        if maze.Maze.get_tile(self.cheese_x, self.cheese_y) == maze.Maze.get_tile(self.x, self.y):
            print("Found!")
            return
        while True:
            dx, dy = self.new_dir
            new_x = self.x + dx * self.speed * delta_time
            new_y = self.y + dy * self.speed * delta_time
            flag = True
            next_tile = Maze.get_tile(new_x, new_y)
            if next_tile is None or isinstance(next_tile, Wall_tile):
                dx = random.random()
                sign1 = random.choice([-1, 1])
                sign2 = random.choice([-1, 1])
                self.new_dir = (sign1 * dx, sign2 * (1 - dx))
                flag = False
            if not flag:
                continue
            else:
                break
        self.x += dx * self.speed * delta_time
        self.y += dy * self.speed * delta_time
