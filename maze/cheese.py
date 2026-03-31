from ui import graphics
class Cheese:
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y

    def draw(self):
        graphics.draw_circle(
            "red",
            self.x,
            self.y,
            2 / 20
        )
