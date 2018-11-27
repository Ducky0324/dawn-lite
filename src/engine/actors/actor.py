import pygame as pg

from engine.util.vec import Vec


class Actor:
    def __init__(self, symbol: str, color: str, pos: Vec):
        self.symbol = symbol
        self.color = pg.Color(color)
        self.pos = pos
        self.isVisible = False


class Hero(Actor):
    def __init__(self, pos: Vec):
        super().__init__('@', "green", pos)
        self.isVisible = True
