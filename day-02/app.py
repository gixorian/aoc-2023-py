class GameSet:
    def __init__(self, red, green, blue):
        self.red = red
        self.green =  green
        self.blue = blue


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
    return id


def getSets(line):
    junk = line.split(":")[0] + ":"
    sets = line.replace(junk, "")\
               .replace("\n", "")\
               .split(";")   
    return sets

def parseGame(sets):
    cubes = [0, 0, 0]
    gameSet = GameSet(0, 0, 0)
    
    for gameSet in sets:
        i = 0

        for _set in gameSet.split(","):
            cubes[i] = _set
            i = i+1

        gameSet = GameSet(cubes[0], cubes[1], cubes[2])

    return gameSet


#cubes = [0, 0, 0]
#print(cubes[0], cubes[1], cubes[2])

for line in Lines:
    currentSet = parseGame(getSets(line))
    print(currentSet.red)

#print(getSets(line))
#print(getID(line))


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
