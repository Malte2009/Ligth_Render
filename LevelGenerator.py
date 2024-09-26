from tempfile import tempdir

from config import config

import time

class LevelGenerator:
    def __init__(self):
        self.level = []

    def generate(self, width, height):
        startTime = time.time()

        for i in range(height):
            self.level.append([0] * width)
        
        endTime = time.time()
        
        print(f"Level generated in {round(endTime - startTime, 2)} seconds")
    
    def setTile(self, x, y, tile):
        self.level[y][x] = tile
    
    def getTile(self, x, y):
        return self.level[y][x]
    
    def get(self):
        return self.level

level = LevelGenerator()