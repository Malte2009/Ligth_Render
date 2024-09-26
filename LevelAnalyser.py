
from config import config
from LevelGenerator import level


class LevelAnalyser:
    def __init__(self):
        self.level = level.get()
    
    def getWallCount(self):
        count = 0

        for y in self.level:
            for x in y:
                if x == config.get().get("defined").get("wall"):
                    count += 1

        return count

    def getWallPositions(self):
        positions = []

        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                if self.level[y][x] == config.get().get("defined").get("wall"):
                    positions.append((x, y))

        return positions

    def getEmptyCount(self):
        count = 0

        for y in self.level:
            for x in y:
                if x == config.get().get("defined").get("nothing"):
                    count += 1

        return count

    def getEmptyPositions(self):
        positions = []

        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                if self.level[y][x] == config.get().get("defined").get("nothing"):
                    positions.append((x, y))

        return positions

    def getLightCount(self):
        count = 0

        for y in self.level:
            for x in y:
                if x == config.get().get("defined").get("light"):
                    count += 1

        return count

    def getLightPositions(self):
        positions = []

        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                if self.level[y][x] == config.get().get("defined").get("light"):
                    positions.append((x, y))

        return positions

    def getTempLightCount(self):
        count = 0

        for y in self.level:
            for x in y:
                if x == config.get().get("defined").get("tempLight"):
                    count += 1

        return count

    def getTempLightPositions(self):
        positions = []

        for y in range(len(self.level)):
            for x in range(len(self.level[y])):
                if self.level[y][x] == config.get().get("defined").get("tempLight"):
                    positions.append((x, y))

        return positions


levelAnalyser = LevelAnalyser()