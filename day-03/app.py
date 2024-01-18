class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Number:

    def __init__(self, x_range, y, value):
        self.x_range = x_range
        self.y = y
        self.value = value
   

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

def GetNumbers():
    x, y = 0, 0
    nums = []
    for line in lines:
        line = line.strip("\n")
        prevC = ""
        for c in line:
            if c.isnumeric():
                if not prevC.isnumeric():
                    nums.append(Number([x], y, c))
                else:
                    nums[-1].x_range.append(x)
                    nums[-1].value += c
            x = x + 1
            prevC = c
        x = 0
        y = y + 1
    return nums

def IsSymbol(character):
    if not character.isnumeric() and character != "." and character != "\n":
        return True
    return False

def GetNeighbours(y, x):
    neighbors = []

    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, 1), (1, -1), (-1, -1)
    ]

    for dy, dx in directions:
        new_y, new_x = y + dy, x + dx

        if 0 <= new_y < len(lines) and 0 <= new_x < len(lines[0]):
            neighbors.append((new_y, new_x))

    return neighbors

def CheckNum(num):
    for x in num.x_range:
        for neighbour in GetNeighbours(num.y, x):
            character = lines[neighbour[0]][neighbour[1]]
            if IsSymbol(character):
                return num
    return None


def GetPartNumbers():
    partNums = []
    for num in GetNumbers():
        if not CheckNum(num) is None:
            partNums.append(num)
    return partNums


def GetPartNumbersOnLine(y):
    nums = []
    for partNum in GetPartNumbers():
        if partNum.y == y:
            nums.append(partNum)
    return nums

def GetPart1Answer():
    sum = 0
    for partNum in GetPartNumbers():
        sum += int(partNum.value)
    return sum

def GetNeighbourPartNumbers(y, x):
    neighbours = GetNeighbours(y, x)
    partNums = GetPartNumbersOnLine(y)
    if y > 0:
        for n in GetPartNumbersOnLine(y-1):
            partNums.append(n)
    if y < len(lines):
        for n in GetPartNumbersOnLine(y+1):
            partNums.append(n)

    gearNums = []
    found = False
    for partNum in partNums:
        partY = partNum.y
        for partX in partNum.x_range:
            for neigbhour in neighbours:
                if neigbhour[0] == partY and neigbhour[1] == partX:
                    gearNums.append(partNum)
                    found = True
                    break
            if found:
                found = False
                break
    return gearNums
            
def GetPart2Answer():
    sum = 0
    y, x = 0, 0
    for line in lines:
        for c in line:
            if c == '*':
                neighbourPartNums = GetNeighbourPartNumbers(y, x)
                if len(neighbourPartNums) == 2:
                    gearRatio = int(neighbourPartNums[0].value) * int(neighbourPartNums[1].value)
                    sum = sum + gearRatio
            x = x + 1
        x = 0
        y = y + 1
    return sum
        
print("Part 1 Answer: " + str(GetPart1Answer()))
print("Part 2 Answer: " + str(GetPart2Answer()))
