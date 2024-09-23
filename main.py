import sys

from level import level
from fileUtil import createFile, writeLevel

sys.setrecursionlimit(10**6)


try:
    devMode = sys.argv[1] == "dev"
except IndexError:
    devMode = False

def main():
    createFile()
    
    if devMode:
        print("Developer mode enabled")
    else:
        print("Developer mode disabled")

        width = int(input("Enter the width of the level: "))
        height = int(input("Enter the height of the level: "))
        
        level.generate(width, height)
        
        overwrite = input("Overwrite the level.json file with the generated level? (y/n): ")
        
        if overwrite.lower() != "y" and overwrite.lower() != "n":
            print("Invalid input")
            return 
        
        if overwrite.lower() == "y":
            writeLevel(level.get())
            print("Level generated and saved to level.json")
            print("You can edit the level.json file to change the level")
            input("Press enter to continue...")

    print("Level generation complete")
    print("Starting rendering...")

if __name__ == '__main__':
    main()
