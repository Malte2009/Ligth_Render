from time import time

from config import config
from fileUtil import readLevel
from LevelGenerator import level
from LevelAnalyser import levelAnalyser

class Engine:
    def __init__(self):
        self.level = readLevel()
        self.levelWidth = len(self.level[0]) - 1
        self.levelHeight = len(self.level) - 1
        self.depth = config.getSettings()["depth"]
        self.currentDepth = 0

        self.startTime = 0
        self.endTime = 0

    def startRender(self):
        self.startTime = time()
        lightSourceCount = levelAnalyser.getLightCount()
        print(lightSourceCount)
        if lightSourceCount == 0:
            return print("No light sources found")

        print(self.generateVector(0, 0, 0, 1))

        self.endTime = time()

        print(f"Rendering completed in {round(self.endTime - self.startTime, 2)} seconds")

    def renderLight(self):
        pass

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

            if x > self.levelWidth or y > self.levelHeight or x < 0 or y < 0:
                break

            cords.append([x, y])

        return cords

    def renderBeam(self):
        pass