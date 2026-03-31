from maze import Maze
from maze.directions import directions
from ui import graphics


class Tile:
    def __init__(self, tile_type, row, column):
        self.tile_type = tile_type
        self.row = row
        self.column = column

    def draw(self):
       pass

    def get_neighb_tile(self, dir_n):
        dx, dy = directions[dir_n]
        return Maze.get_tile(self.column + 0.5 + dx, self.row + 0.5 + dy)

    @staticmethod
    def static_get_neighb_tile(x, y, dir_n):
        dx, dy = directions[dir_n]
        return Maze.get_tile(y + 0.5 + dy, x + 0.5 + dx)

    @staticmethod
    def dist_to_border(x, y, dir_n):
        x -= int(x)
        y -= int(y)
        if dir_n == 0:
            return 1 - x
        elif dir_n == 1:
            return y
        elif dir_n == 2:
            return x
        return 1 - y


class Wall_tile(Tile):
    def __init__(self, row, column):
        super().__init__("1", row, column)
        self.image = graphics.load_image("images/wall.png")

    def draw(self):
        graphics.draw_image(self.image, self.column, self.row)


class Room_tile(Tile):
    def __init__(self, row, column):
        super().__init__("0", row, column)

# пустая комната не нуждается в рисовании
