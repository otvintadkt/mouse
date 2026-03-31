import random
from maze.tiles import Room_tile, Wall_tile

class PrimMaze:
    # на сколько можно сдвигаться
    side_directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    corner_directions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        # Статус клетки лабиринта: 0 - не путь, 1 - путь
        self.cell_status = tuple([0 for _ in range(m)] for _ in range(n))
        # Начальная клетка
        self.cell_status[0][0] = 1
        # Подсчёт количества соседей по сторонам клетки. Нужно для того, чтобы не было циклов
        self.cnt_side_neighbours = tuple([0 for _ in range(m)] for _ in range(n))

    def update_neighbours(self, cell: tuple[int, int], neighbours: set):
        for direction in self.side_directions:
            new_cell = (cell[0] + direction[0], cell[1] + direction[1])
            if not self.in_field(new_cell): continue
            self.cnt_side_neighbours[new_cell[0]][new_cell[1]] += 1
            neighbours.add(new_cell)

    def in_field(self, cell: tuple[int, int]):
        if 0 <= cell[0] < self.n and 0 <= cell[1] < self.m:
            return True
        return False

    def is_placement_ok(self, cell: tuple[int, int]):
        # Смотрим клетки, расположенные по диагонали от данной
        for direction in self.corner_directions:
            new_cell = (cell[0] + direction[0], cell[1] + direction[1])
            if not self.in_field(new_cell): continue
            # Если угловая клетка является частью пути и боковые клетки не
            # являются его частью, то нарушается идеальность лабиринта
            side_cell_1 = (new_cell[0], cell[1])
            side_cell_2 = (cell[0], new_cell[1])
            if self.cell_status[new_cell[0]][new_cell[1]] == 1 and \
                    self.cell_status[side_cell_1[0]][side_cell_1[1]] == 0 and \
                    self.cell_status[side_cell_2[0]][side_cell_2[1]] == 0:
                return False
        return True

    def Prim(self):
        # Соседи первой части (клеток пути), которых мы пытаемся присое
        neighbours = {(0, 0)}
        self.update_neighbours((0, 0), neighbours)
        while neighbours:
            list_neighbours = list(neighbours)
            random.shuffle(list_neighbours)
            neighbours = set(list_neighbours)
            cell = neighbours.pop()
            # Если клетка вне лабиринта - пропускаем
            if not self.in_field(cell): continue
            # Если клетка уже путь - пропускаем
            if self.cell_status[cell[0]][cell[1]] == 1: continue
            # Если размещение клетки приведёт к нарушению идельности лабиринта - пропускаем
            if not self.is_placement_ok(cell): continue
            if self.cnt_side_neighbours[cell[0]][cell[1]] >= 2: continue
            # Все условия в порядке - помечаем как путь
            self.cell_status[cell[0]][cell[1]] = 1
            # Обновляем к-во соседей для соседей новой клетки пути
            self.update_neighbours(cell, neighbours)

    def visualise(self):
        for row in self.cell_status:
            for cell in row:
                # Путь
                if cell == 1:
                    print("0", end="")
                # Не путь
                else:
                    print("1", end="")
            print()


def get_maze():
    n = random.randint(5, 8)
    m = random.randint(5, 8)
    maze = PrimMaze(n, m)
    maze.Prim()
    new_maze = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            new_maze[i + 1][j + 1] = maze.cell_status[i][j]
    for i in new_maze:
        print(*i)

    maze = []
    for i, row in enumerate(new_maze):
        maze.append([])
        for j, cell in enumerate(row):
            if cell == 1:
                maze[i].append(Room_tile(i, j))
            else:
                maze[i].append(Wall_tile(i, j))
    return maze

