from tempfile import tempdir

from config import config

import time

class LevelGenerator:

    def generate(self, width, height):
        startTime = time.time()
        file = open("level.json", "a")
        file.write("[\n")

        for i in range(height):
            if i == height - 1:
                file.write(f"{[config.getDefined().get("nothing")] * width}")
            else:
                file.write(f"{[config.getDefined().get("nothing")] * width},\n")

        file.write("\n]")
        file.close()
        endTime = time.time()
        
        print(f"Level generated in {round(endTime - startTime, 2)} seconds")
    
    def setTile(self, x, y, tile):
        self.level[y][x] = tile
    
    def getTile(self, x, y):
        return self.level[y][x]


level = LevelGenerator()