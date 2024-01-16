# xStart xEnd
# y


# line Y
# c X

class Number:

    def __init__(self, x_start, x_end, y, value):
        self.x_start = x_start
        self.x_end = x_end
        self.y = y
        self.value = value
    
    def getRange(self):
        xRange = []
        for i in range(self.x_start, self.x_end+1):
            xRange.append(i)
        return xRange
   

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

x, y = 0, 0
xStart, xEnd = 0, 0
nums = []
num = ""
for line in lines:
    line = line.strip("\n")
    
    for c in line:
        #print("\nx: " + str(x) + ", y: " + str(y))
        
        if c.isnumeric():
            if num == "":
                xStart = x
            else:
                xEnd = x
            num += c
        else:
            #print(str(xStart) + "-" + num + "-" + str(xEnd))
            if num != "":
                nums.append(Number(xStart, xEnd, y, int(num)))
            num = ""
        
        x = x + 1
    
    x = 0
    y = y + 1

def IsSymbol(character):
    if not character.isnumeric() and character != ".":
        return True
    return False

def GetNeighbours(x, y):
    neighbours = []
    if y > 0:
        neighbours.append(lines[y-1][x])
        if x > 0:
            neighbours.append(lines[y-1][x-1])
        if x < len(lines[y]):
            neighbours.append(lines[y-1][x+1])
    if y < len(lines):
        neighbours.append(lines[y+1][x])
        if x > 0:
            neighbours.append(lines[y+1][x-1])
        if x < len(lines[y]):
            neighbours.append(lines[y+1][x+1])
    if x > 0:
        neighbours.append(lines[y][x-1])
    if x < len(lines[y]):
        neighbours.append(lines[y][x+1])



def GetPartNums():
    sum = 0
    for num in nums:
        y = num.y
        for x in num.getRange():
            if IsSymbol(lines[y-1][x-1]) or IsSymbol(lines[y-1][x]) or IsSymbol(lines[y-1][x+1]) or IsSymbol(lines[y][x-1]) or IsSymbol(lines[y][x]) or IsSymbol(lines[y][x+1]) or IsSymbol(lines[y+1][x-1]) or IsSymbol(lines[y+1][x]) or IsSymbol(lines[y+1][x+1]):
                sum += num.value        
    return sum

print(GetPartNums())
#  467..114..
#  ...*......
#  ..35..633.
#  ......#...
#  617*......
#  .....+.58.
#  ..592.....
#  ......755.
#  ...$.*....
#  .664.598..
