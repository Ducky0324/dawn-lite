import pygame as pg
from os import path

import engine.constants as constants
from engine.camera import Camera
from engine.stage.stage import Stage
from engine.stage.tile_type import Tiles
from engine.util.vec import Vec, Directions
from engine.actors.actor import Hero


class Engine:
    def __init__(self, winWidth, winHeight):
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.cols = winWidth // constants.TILE_SIZE
        self.rows = winHeight // constants.TILE_SIZE

        pg.init()
        pg.mixer.init()
        pg.display.set_caption("dawn-lite")
        pg.key.set_repeat(10, 50)

        self.stage = Stage(self.cols * 2, self.rows * 2)

        self.stage.fillWith(Tiles.wall)
        for x in range(1, self.stage.width - 1):
            for y in range(1, self.stage.height - 1):
                pos = Vec(x, y)
                self.stage.setTile(pos, Tiles.floor)

        self.font = pg.font.Font(path.join(constants.FONT_PATH,
                                           constants.DEFAULT_FONT),
                                 constants.TILE_SIZE)

        self.player = Hero(Vec(60, 3))
        self.stage.addActor(self.player)

        self.camera = Camera(self, self.stage, self.cols, self.rows)
        self.camera.update(self.player)

        self.window = pg.display.set_mode((self.winWidth, self.winHeight))
        self.clock = pg.time.Clock()
        self.running = True

    def start(self):
        while self.running:
            self.handleEvents()
            self.update()
            self.render()

    def handleEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_w:
                    if self.stage.rows == self.camera.height:
                        return
                    self.stage.moveActor(self.player, Directions.N)
                    self.player.pos = self.player.pos + Directions.N

                if event.key == pg.K_a:
                    if self.stage.cols == self.camera.width:
                        return
                    self.stage.moveActor(self.player, Directions.W)
                    self.player.pos = self.player.pos + Directions.W

                if event.key == pg.K_s:
                    if self.stage.rows == self.camera.height:
                        return
                    self.stage.moveActor(self.player, Directions.S)
                    self.player.pos = self.player.pos + Directions.S

                if event.key == pg.K_d:
                    if self.stage.cols == self.camera.width:
                        return
                    self.stage.moveActor(self.player, Directions.E)
                    self.player.pos = self.player.pos + Directions.E
                self.camera.update(self.player)
                print(self.camera.bounds)

    def drawGlyphAt(self, glyph, x, y):
        self.window.blit(glyph,
                         (x * constants.TILE_SIZE,
                          y * constants.TILE_SIZE))

    def _drawStage(self):
        # Loop through the positions in range of the camera's rect
        for pos in self.camera:
            tile = self.stage[pos]
            actor = self.stage.getActorAt(pos)
            if tile.isVisible:
                symbol = tile.type.symbol
                fore = tile.type.explored[0]
                back = tile.type.explored[1]
                glyph = self.font.render(symbol, True, fore, back)
                self.drawGlyphAt(glyph,
                                 pos.x - self.camera.bounds.x,
                                 pos.y - self.camera.bounds.y)
            if tile.isExplored:
                symbol = tile.type.symbol
                fore = tile.type.explored[0]
                back = tile.type.explored[1]
                glyph = self.font.render(symbol, True, fore, back)
                self.drawGlyphAt(glyph,
                                 pos.x - self.camera.bounds.x,
                                 pos.y - self.camera.bounds.y)
            if actor is not None and actor.isVisible:
                symbol = actor.symbol
                color = actor.color
                glyph = self.font.render(symbol, True, color)
                self.drawGlyphAt(glyph,
                                 pos.x - self.camera.bounds.x,
                                 pos.y - self.camera.bounds.y)

    def update(self):
        pass

    def render(self):
        self._drawStage()
        pg.display.flip()
