import sys

import os

from LevelGenerator import level
from config import config
from fileUtil import createFile, writeLevel

sys.setrecursionlimit(10**6)


try:
    devMode = sys.argv[1] == "dev"
except IndexError:
    devMode = False

def main():
    if not os.path.exists("level.json"):
        createFile()

    if devMode:
        print("Developer mode enabled")
    else:
        print("Developer mode disabled")

        width = int(input("Enter the width of the level: "))

        if width > config.getSettings()["maxSize"]:
            print(f"Width cannot be greater than {config.getSettings()['maxSize']}")
            input("Press enter to exit...")
            sys.exit()

        height = int(input("Enter the height of the level: "))

        if height > config.getSettings()["maxSize"]:
            print(f"Height cannot be greater than {config.getSettings()['maxSize']}")
            input("Press enter to exit...")
            sys.exit()

        level.generate(width, height)

        writeLevel(level.level)

        print("Level generated and saved to level.json")
        print("You can edit the level.json file to change the level")
        input("Press enter to continue...")

    print("Starting rendering...")

    from RenderEngine import Engine

    engine = Engine()

    if engine.startRender() is False:
        print("Rendering failed")
        input("Press enter to exit...")
        sys.exit()

    engine.render()


if __name__ == '__main__':
    main()
