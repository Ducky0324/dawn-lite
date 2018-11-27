

class Tile:
    def __init__(self, tileType):
        self.type = tileType
        self.isExplored = True
        self.isVisible = False

    def setVisible(self, visible: bool):
        self.isVisible = visible

        if self.isVisible and not self.isExplored:
            self.isExplored = True

    def __repr__(self):
        return self.type.symbol
