from pygame import Color


class TileType:
    def __init__(self,
                 symbol: str,  # The symbol that will display for the tile
                 walkable: bool,  # Whether or not you can walk on the tile
                 visible: list,  # Color when tile is in FOV
                 explored: list):  # Color when tile has been explored and is out of FOV
        self.symbol = symbol
        self.visible = [Color(c) for c in visible]
        self.explored = [Color(c) for c in explored]
        self.walkable = walkable


class Tiles:

    """
    <tile_name> = TileType("<glyph>",
                           visible=[<foreground>, <background>],
                           explored=[<foreground>, <background>])
    The foreground and background can be either the names of the colors (as strings)
    or (r, g, b) / (r, g, b, a) tuples
    """

    floor = TileType(".",
                     walkable=True,
                     visible=["white", "black"],
                     explored=["grey", "black"])

    wall = TileType("#",
                    walkable=False,
                    visible=["black", "grey"],
                    explored=["grey", "black"])
