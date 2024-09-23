import tomlUtil as config


class Level:
    def __init__(self):
        self.level = []
    
    
    def generate(self, width, height):
        for i in range(height):
            self.level.append([config.read().get("defined").get("nothing")] * width)
    
    def setTile(self, x, y, tile):
        self.level[y][x] = tile
    
    def getTile(self, x, y):
        return self.level[y][x]
    
    def get(self):
        return self.level
    
    def set(self, level):
        self.level = level


level = Level()