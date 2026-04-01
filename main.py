import maze.Maze
import settings
import ui.graphics
from maze import Maze
from ui import events
from ui import graphics
from maze.tiles import Wall_tile
import random

FPS = 60
running = True
clock = events.Clock()

is_moving = False
last_mouse_pos = [0, 0]

while running:
    for event in events.get_event_queue():
        # print(random.randint(1, 4))
        if event.type == events.QUIT:
            running = False
        if event.type == events.MOUSEBUTTONDOWN:
            if event.button == 1:
                Maze.add_mouse(
                    (event.pos[0] - settings.view_left_top[0]) / settings.tile_size[0],
                    (event.pos[1] - settings.view_left_top[1]) / settings.tile_size[1]
                )
                if Maze.cheese is not None:
                    Maze.mouse.goto_cheese(Maze.cheese.x, Maze.cheese.y)
            if event.button == 3:
                Maze.add_cheese(
                    (event.pos[0] - settings.view_left_top[0]) // settings.tile_size[0] + 1 / 2,
                    (event.pos[1] - settings.view_left_top[1]) // settings.tile_size[1] + 1 / 2
                )
                if Maze.mouse is not None:
                    Maze.mouse.goto_cheese(Maze.cheese.x, Maze.cheese.y)
            if event.button == 2 and maze.Maze.get_tile(
                    (event.pos[0] - settings.view_left_top[0]) / settings.tile_size[0],
                    (event.pos[1] - settings.view_left_top[1]) / settings.tile_size[1]
            ):
                is_moving = True
                last_mouse_pos = event.pos
        elif event.type == events.MOUSEBUTTONUP and event.button == 2:
            is_moving = False
        elif event.type == events.MOUSEMOTION and is_moving:
            settings.view_left_top[0] += event.pos[0] - last_mouse_pos[0]
            settings.view_left_top[1] += event.pos[1] - last_mouse_pos[1]
            last_mouse_pos = event.pos
        elif event.type == events.MOUSEWHEEL:
            coef = 1 + 0.1 * event.y
            settings.tile_size[0] *= coef
            settings.tile_size[1] *= coef
            settings.size[0] *= coef
            settings.size[1] *= coef
            ui.graphics.load_image("images/wall.png")

    graphics.fill("black")
    # рисуем лабиринт
    Maze.draw()
    graphics.flip()
    clock.tick(FPS)
    # обновляем весь лабиринт
    Maze.update(1 / FPS)
