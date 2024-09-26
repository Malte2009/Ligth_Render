import json


def createFile():
    file = open("level.json", "w")
    file.close()

def writeLevel(level):
    file = open("level.json", "w")

    file.write("[\n")
    for i in range(len(level)):
        file.write(str(level[i]))
        if i != len(level) - 1:
            file.write(",")
        file.write("\n")
    file.write("]")
    file.close()

def readLevel():
    file = open("level.json", "r")
    level = json.loads(file.read())
    file.close()

    return level
