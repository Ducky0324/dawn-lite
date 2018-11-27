import pygame as pg
from engine.util.vec import Vec


class Camera:
    def __init__(self, engine, stage, width, height):
        self.width, self.height = width, height
        self.stage = stage
        self.screenCols = engine.cols
        self.screenRows = engine.rows
        self.bounds = pg.Rect(0,
                              0,
                              self.width,
                              self.height)

    def __iter__(self):
        return (Vec(x, y)
                for x in range(self.bounds.x, self.bounds.x + self.bounds.width)
                for y in range(self.bounds.y, self.bounds.y + self.bounds.height))

    def update(self, target):
        x = -target.pos.x + (self.screenCols // 2)
        y = -target.pos.y + (self.screenRows // 2)

        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - self.stage.cols) - 1, x)
        y = max(-(self.height - self.stage.rows), y)
        self.bounds = pg.Rect(-x, -y, self.width, self.height)
