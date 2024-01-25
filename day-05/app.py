import time

######################################################

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

######################################################

p1Seeds = []
p2Seeds = []
index = 0
maps = [[], [], [], [], [], [], []]

for line in lines:
    line = line.strip("\n")
    if "seeds:" in line:
        line = line.strip("seeds: ")
        p1Seeds = line.split(" ")
        for i in range(0, len(p1Seeds), 2):
            p2Seeds.append(
                (int(p1Seeds[i]), int(p1Seeds[i]) + int(p1Seeds[i + 1]) - 1, 0)
            )
    elif "seed-to-soil map:" in line:
        index = 0
    elif "soil-to-fertilizer map:" in line:
        index = 1
    elif "fertilizer-to-water map:" in line:
        index = 2
    elif "water-to-light map:" in line:
        index = 3
    elif "light-to-temperature map:" in line:
        index = 4
    elif "temperature-to-humidity map:" in line:
        index = 5
    elif "humidity-to-location map:" in line:
        index = 6
    elif line == "":
        continue
    else:
        maps[index].append(line.split(" "))


def GetPart1Answer():
    start_time = time.time()

    mappingNumber = 0
    rangeOffset = 0
    locations = []

    for seed in p1Seeds:
        mappingNumber = int(seed)
        for map in maps:
            for mapRanges in map:
                if mappingNumber >= int(mapRanges[1]) and int(mappingNumber) < int(
                    mapRanges[1]
                ) + int(mapRanges[2]):
                    rangeOffset = mappingNumber - int(mapRanges[1])
                    mappingNumber = int(mapRanges[0]) + rangeOffset
                    break
        locations.append(mappingNumber)

    return (min(locations), str(format((time.time() - start_time) * 1000, ".2f")))


def GetPart2Answer():
    start_time = time.time()
    lowestLocation = float("inf")

    while p2Seeds:
        seedStart, seedEnd, seedDepth = p2Seeds.pop(0)
        depth = 0
        canContinue = False

        for map in maps:
            if seedDepth == depth or canContinue:
                canContinue = True

                for mapRange in map:
                    sourceRangeStart = int(mapRange[1])
                    sourceRangeEnd = int(mapRange[1]) + int(mapRange[2])
                    targetRangeStart = int(mapRange[0])

                    if seedStart >= sourceRangeStart and seedEnd < sourceRangeEnd:
                        # The whole range is in the mapped range
                        seedStart = targetRangeStart + (seedStart - sourceRangeStart)
                        seedEnd = targetRangeStart + (seedEnd - sourceRangeStart)
                        break
                    elif seedStart >= sourceRangeStart and seedStart < sourceRangeEnd and seedEnd >= sourceRangeEnd:
                        # The whole range is not in the mapped range, need to split it, extra is on the right
                        p2Seeds.append((sourceRangeEnd, seedEnd, depth))
                        seedStart = targetRangeStart + (seedStart - sourceRangeStart)
                        seedEnd = targetRangeStart + (sourceRangeEnd - 1 - sourceRangeStart)
                        break
                    elif seedStart < sourceRangeStart and seedEnd > sourceRangeStart and seedEnd <= sourceRangeEnd:
                        # The whole range is not in the mapped range, need to split it, extra is on the left
                        p2Seeds.append((seedStart, sourceRangeStart - 1, depth))
                        seedStart = targetRangeStart + (sourceRangeStart - sourceRangeStart)
                        seedEnd = targetRangeStart + (seedEnd - sourceRangeStart)
                        break

            depth += 1

        if seedStart < lowestLocation:
            lowestLocation = seedStart

    return (str(lowestLocation), str(format((time.time() - start_time) * 1000, ".2f")))


res, fTime = GetPart1Answer()
print("Part 1 Answer: " + str(res) + " in " + str(fTime) + " ms")
print("")

res, fTime = GetPart2Answer()
print("Part 2 Answer: " + res + " in " + fTime + " ms")
