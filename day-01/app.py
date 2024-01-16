# Set up the dict to map digits spelled out with letters to integers
digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# Function to check if a substring is a digit. If it is, return the integer digit, if not return -1
def convertDigit(strline):
    for digit in digits:
        if digit in strline:
            return digits[digit]
    return -1


# Main function that converts the line into an integer like (first digit * 10 + last digit)
def convertLine(line):
    fd = -1
    ld = -1
    tempstr = ""
    for c in line:
        tempstr += c
        n = -1
        n = convertDigit(tempstr)
        if c.isnumeric():
            n = int(c)
        if n != -1:
            if fd == -1:
                fd = n
            ld = n
            tempstr = c
    return (fd * 10) + ld


# Open the file and load the lines into a list of strings
inputFile = open("input.txt", "r")
Lines = inputFile.readlines()
inputFile.close()

sum = 0

# Go trough the list, convert the lines into integers and add them all together
for line in Lines:
    sum += int(convertLine(line))

# print the result
print(sum)
