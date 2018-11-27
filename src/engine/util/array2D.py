from .vec import Vec


class Array2D:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.items = [[None for _ in range(self.width)]
                      for _ in range(self.height)]

    def fill(self, item):
        self.items = [[item for x in range(self.width)]
                      for y in range(self.height)]

    def __iter__(self):
        return (Vec(x, y) for x in range(self.width) for y in range(self.height))

    def __getitem__(self, index: Vec):
        return self.items[index.y][index.x]

    def __setitem__(self, index: Vec, item):
        self.items[index.y][index.x] = item

    def __repr__(self):
        for row in self.items:
            print(row)
        return ""
