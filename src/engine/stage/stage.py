import pygame as pg
import engine.constants as constants

from engine.util.array2D import Array2D
from engine.util.vec import Vec
from engine.stage.tile import Tile
from engine.stage.tile_type import TileType


class Stage:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cols = self.width // constants.TILE_SIZE
        self.rows = self.height // constants.TILE_SIZE
        self.bounds = pg.Rect(0, 0, self.width, self.height)
        self.tiles = Array2D(width, height)
        self.actors = Array2D(width, height)

    def fillWith(self, tile_type: TileType):
        self.tiles.fill(Tile(tile_type))

    def inBounds(self, pos: Vec):
        return self.bounds.collidepoint(pos.x, pos.y)

    def getTile(self, pos: Vec) -> TileType:
        return self.tiles[pos].type

    def setTile(self, pos: Vec, new_type: TileType):
        self.tiles[pos] = Tile(new_type)

    def addActor(self, actor):
        self.actors[actor.pos] = actor

    def moveActor(self, actor, direction):
        self.actors[actor.pos] = None
        self.actors[actor.pos + direction] = actor

    def getActorAt(self, pos: Vec):
        return self.actors[pos]

    def removeActor(self, actor):
        self.actors[actor.pos] = None

    def __getitem__(self, pos: Vec):
        return self.tiles[pos]

    def __repr__(self):
        print(self.tiles)
        return ""
