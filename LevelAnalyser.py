
from config import config
from fileUtil import readLevel


class LevelAnalyser:

    def getWallCount(self, level):
        count = 0

        for y in level:
            for x in y:
                if x == config.get().get("defined").get("wall"):
                    count += 1

        return count

    def getWallPositions(self, level):
        positions = []

        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == config.get().get("defined").get("wall"):
                    positions.append((x, y))

        return positions

    def getEmptyCount(self, level):
        count = 0

        for y in level:
            for x in y:
                if x == config.get().get("defined").get("nothing"):
                    count += 1

        return count

    def getEmptyPositions(self, level):
        positions = []

        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == config.get().get("defined").get("nothing"):
                    positions.append((x, y))

        return positions

    def getLightSourceCount(self, level):
        count = 0

        for y in level:
            for x in y:
                if x == config.get().get("defined").get("lightSource"):
                    count += 1

        return count

    def getLightSourcePositions(self, level):
        positions = []

        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == config.getDefined().get("lightSource"):
                    positions.append([x, y])

        return positions

    def getTempLightSourceCount(self, level):
        count = 0

        for y in level:
            for x in y:
                if x == config.get().get("defined").get("tempLightSource"):
                    count += 1

        return count

    def getTempLightSourcePositions(self, level):
        positions = []

        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == config.getDefined().get("tempLightSource"):
                    positions.append([x, y])

        return positions


levelAnalyser = LevelAnalyser()