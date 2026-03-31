from maze.generateMaze import get_maze
from maze.mice import SmartMouse
from maze import cheese as Cheese

mouse = None
cheese = None
maze = get_maze()

# Рисуем все: и тайлы и мышей
def draw():
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            maze[row][column].draw()

    if mouse is not None:
        mouse.draw()
    
    if cheese is not None:
        cheese.draw()


# Получаем тайл по координатам лабиринта
def get_tile(x, y):
    if 0 <= y < len(maze) and 0 <= x < len(maze[int(y)]):
        tile_column, tile_row = int(x), int(y)
        return maze[tile_row][tile_column]
    else:
        return None


# двигаем, все что движется
# вызов этой функции постоянно в цикле в main.py
def update(delta_time):
    if mouse is not None:
        mouse.update(delta_time)


def add_mouse(x, y):
    global mouse
    mouse = SmartMouse(x, y)

def add_cheese(x, y):
    global cheese
    cheese = Cheese.Cheese(x, y)
