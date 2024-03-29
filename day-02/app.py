class GameSet:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def getPower(self):
        return self.red * self.green * self.blue


inputFile = open("input.txt", "r")
Lines = inputFile.readlines()
inputFile.close()

bag = {
    "red":   12,
    "green": 13,
    "blue":  14
}

def getID(line):
    id = line.split(":")[0].replace("Game ", "")
    return int(id)


def getSets(line):
    junk = line.split(":")[0] + ":"
    sets = line.replace(junk, "")\
               .replace("\n", "")\
               .split(";")   
    return sets


def getCubes(_set):
    gameSet = GameSet()
    cubes = _set.split(",")
    for cube in cubes:
        if "red" in cube:
            gameSet.red = int(cube.replace(" red", "").replace(" ", ""))
        if "green" in cube:
            gameSet.green = int(cube.replace(" green", "").replace(" ", ""))
        if "blue" in cube:
            gameSet.blue = int(cube.replace(" blue", "").replace(" ", ""))
    return gameSet


def GetPart1Result():
    result = 0
    for line in Lines:
        isPossible = False

        for _set in getSets(line):
            cubes = getCubes(_set)
            if cubes.red <= bag["red"] and cubes.green <= bag["green"] and cubes.blue <= bag["blue"]:
                isPossible = True
            else:
                isPossible = False
                break
        
        if isPossible:
            result += getID(line)
    return result

def GetPart2Result():
    result = 0
    for line in Lines:
        power = 0
        lowestSet = GameSet()
        
        for _set in getSets(line):
            cubes = getCubes(_set)
            if cubes.red > lowestSet.red:
                lowestSet.red = cubes.red
            if cubes.green > lowestSet.green:
                lowestSet.green = cubes.green
            if cubes.blue > lowestSet.blue:
                lowestSet.blue = cubes.blue

        power = lowestSet.getPower()
        result += power
    return result

print("Part 1 result: " + str(GetPart1Result()))
print("Part 2 result: " + str(GetPart2Result()))
  



# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
