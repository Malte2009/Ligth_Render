from time import time

from config import config
from fileUtil import readLevel
from LevelAnalyser import levelAnalyser


level = readLevel()

class Engine:
    def __init__(self):
        self.levelWidth = len(level[0])
        self.levelHeight = len(level)
        self.depth = config.getSettings()["depth"]
        self.currentDepth = 0

        self.startTime = 0
        self.endTime = 0

    def startRender(self):

        level[5][5] = config.getDefined()["lightSource"]

        lightSourceCount = levelAnalyser.getLightSourceCount(level)

        if lightSourceCount == 0:
            print("No light sources found")
            return False

        self.startTime = time()

        self.renderLight(True)

        self.endTime = time()

        print(f"Rendering completed in {round(self.endTime - self.startTime, 5)} seconds")

    def render(self):
        for y in level:
            for x in y:
                if x == config.getDefined()["nothing"]:
                    print(" ", end=" ")
                elif x == config.getDefined()["wall"]:
                    print("#", end=" ")
                elif x == config.getDefined()["light"]:
                    print("1", end=" ")
                elif x == config.getDefined()["lightSource"]:
                    print("L", end=" ")
                elif x == config.getDefined()["tempLightSource"]:
                    print("T", end=" ")
                else:
                    print("?", end=" ")

            print()

    def renderLight(self, main: bool):

        if self.currentDepth >= self.depth:
            return

        if levelAnalyser.getEmptyPositions(level) == 0:
            print("No empty positions found")
            return

        self.currentDepth += 1

        if main:
            lightSources = levelAnalyser.getLightSourcePositions(level)

            for lightSource in lightSources:
                x = lightSource[0]
                y = lightSource[1]

                for cord in self.getSurroundingTiles(x, y):
                    xDirection = cord[0] - x
                    yDirection = cord[1] - y

                    self.renderBeam(x, y, xDirection, yDirection)
        else:
            tempLightSources = levelAnalyser.getTempLightSourcePositions(level)

            for tempLightSource in tempLightSources:
                x = tempLightSource[0]
                y = tempLightSource[1]

                for cord in self.getSurroundingTiles(x, y):
                    xDirection = cord[0] - x
                    yDirection = cord[1] - y

                    level[y][x] = config.getDefined()["light"]
                    self.renderBeam(x, y, xDirection, yDirection)

        tempLightSources = levelAnalyser.getTempLightSourceCount(level)

        if tempLightSources > 0:
            self.renderLight(False)


    def getSurroundingTiles(self, xPos, yPos):
        #TODO: Test if dicts would be faster than lists
        cords = []


        for y in range(yPos - 1, yPos + 2):
            for x in range(xPos - 1, xPos + 2):
                if x == xPos and y == yPos:
                    continue


                cords.append([x, y])

        return cords

    def generateVector(self, xStart, yStart, xDirection, yDirection):
        #TODO: Test if dicts would be faster than lists (prob not)
        cords = []

        x = xStart
        y = yStart

        while True:
            x += xDirection
            y += yDirection

            if (       x >= self.levelWidth
                    or y >= self.levelHeight
                    or x < 0
                    or y < 0
                    or level[y][x] == config.getDefined()["wall"]):
                break

            cords.append([x, y])

        return cords

    def renderBeam(self, xStart, yStart, xDirection, yDirection):
        cords = self.generateVector(xStart, yStart, xDirection, yDirection)

        for cord in cords:
            if cord == cords[len(cords) - 1] and level[cord[1]][cord[0]] == config.getDefined()["nothing"]:
                level[cord[1]][cord[0]] = config.getDefined()["tempLightSource"]
                return


            if level[cord[1]][cord[0]] == config.getDefined()["nothing"]:
                level[cord[1]][cord[0]] = config.getDefined()["light"]