import os
import concurrent.futures

######################################################

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

######################################################

seeds = []
index = 0
maps = [[],[],[],[],[],[],[]]

for line in lines:
    line = line.strip("\n")
    if "seeds:" in line:
        line = line.strip("seeds: ")
        seeds = line.split(" ")
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
    mappingNumber = 0
    rangeOffset = 0
    locations = []
    for seed in seeds:
        mappingNumber = int(seed)
        for map in maps:
            for mapRanges in map:
                if mappingNumber >= int(mapRanges[1]) and int(mappingNumber) < int(mapRanges[1])+int(mapRanges[2]):
                    rangeOffset = mappingNumber - int(mapRanges[1])
                    mappingNumber = int(mapRanges[0]) + rangeOffset
                    break
        locations.append(mappingNumber)    
    return min(locations)


### OPTIMIZATION:
### Go in reverse
### Go trough the locations first in order of lowest to highest
### That way, unless the smallest possible location is near the end, it should be much faster

### Even better idea (not sure if possible though)
### Go trough all of the ranges first, and once we find which range contains the lowest location or reverse, depending on what's better and possible...
### Than we just need to go trough all seeds or locations in that range

### The fastest would probably be to combine the ideas
### Go trough all of the location ranges first, starting with the lowest range
### As soon as we find a sees/seed range that fits the location range, we go trough all of the locations in that range, stasrting with the lowest one again
### This way we should be able to find the range without needing to go trough all of them, and then find the seed without needing to go trough all of them as well


def GetPart2Answer():
    mappingNumber = 0
    rangeOffset = 0
    locations = []
    for seedIndex in range(0, len(seeds), 2):
        if seedIndex < len(seeds)-1:
            seedMax = int(seeds[seedIndex])+int(seeds[seedIndex+1])
        else:
            seedMax = int(seeds[seedIndex])+1
            
        for seedNum in range(int(seeds[seedIndex]), seedMax): 
            mappingNumber = seedNum
            if mappingNumber % 1000 == 0:
                os.system('clear')
            for map in maps:
                for mapRanges in map:
                    if mappingNumber >= int(mapRanges[1]) and int(mappingNumber) < int(mapRanges[1])+int(mapRanges[2]):
                        rangeOffset = mappingNumber - int(mapRanges[1])
                        mappingNumber = int(mapRanges[0]) + rangeOffset
                        break
            locations.append(mappingNumber)    
        return min(locations) 


def locationMap(mappingNumber):
    location = mappingNumber
    if mappingNumber % 10000 == 0:
        os.system('clear')
        print(location)
    for map in range(len(maps)-1, -1, -1):
        for mapRange in maps[map]:
            rangeStart = int(mapRange[0])
            rangeEnd = int(mapRange[0]) + int(mapRange[2])
            if mappingNumber >= rangeStart and mappingNumber < rangeEnd:
                rangeOffset = mappingNumber - int(mapRange[0])
                mappingNumber = int(mapRange[1]) + rangeOffset
                break

    for i in range(0, len(seeds), 2):
        if mappingNumber >= int(seeds[i]) and mappingNumber < int(seeds[i]) + int(seeds[i+1]):
            return location

def GetParallelPart2Answer():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(locationMap, mappingNumber) for mappingNumber in range(20000000, 1000000000)]

        results = [future.result() for future in concurrent.futures.as_completed(futures)]
        return results


def GetReversePart2Answer():
    rangeOffset = 0
    for mappingNumber in range(1000000, 1000000000):
        location = mappingNumber
        if mappingNumber % 1000 == 0:
            os.system('clear')
            print(location)
        for map in range(len(maps)-1, -1, -1):
            for mapRange in maps[map]:
                rangeStart = int(mapRange[0])
                rangeEnd = int(mapRange[0]) + int(mapRange[2])
                if mappingNumber >= rangeStart and mappingNumber < rangeEnd:
                    rangeOffset = mappingNumber - int(mapRange[0])
                    mappingNumber = int(mapRange[1]) + rangeOffset
                    break

        for i in range(0, len(seeds), 2):
            if mappingNumber >= int(seeds[i]) and mappingNumber < int(seeds[i]) + int(seeds[i+1]):
                return location


def GetOptimizedPart2Answer():
    mappingNumber = 0
    rangeOffset = 0
    locations = []
    remaining = []
    for i in range(0, len(seeds), 2):
        seedStart = int(seeds[i])
        seedEnd = int(seeds[i]) + int(seeds[i+1]) - 1

        for map in maps:
            for mapRange in map:
                sourceRangeStart = int(mapRange[1])
                sourceRangeEnd = int(mapRange[1]) + int(mapRange[2])
                targetRangeStart = int(mapRange[0])
                targetRangeEnd = int(mapRange[0]) + int(mapRange[2])
                print(i)
                #print("seedEnd: {}, targetRangeStart: {} + ( seedEnd: {} - sourceRangeStart: {}, )".format(seedEnd, targetRangeStart, seedEnd, sourceRangeStart))
                if seedStart >= sourceRangeStart and seedEnd < sourceRangeEnd:
                    #The whole range is in the mapped range
                    print("source start: {}, source end: {}".format(seedStart,seedEnd))
                    seedStart = targetRangeStart + (seedStart - sourceRangeStart)
                    seedEnd = targetRangeStart + (seedEnd - sourceRangeStart)
                    print("target start: {}, target end: {}".format(seedStart,seedEnd))  
                    break
                elif seedStart >= sourceRangeStart and seedStart < sourceRangeEnd and seedEnd >= sourceRangeEnd:
                    #The whole range is not in the mapped range, need to split it, extra is on the right 
                    print("source start: {}, source end: {}".format(seedStart,seedEnd))
                    remaining.append((sourceRangeEnd, seedEnd))
                    seedStart = targetRangeStart + (seedStart - sourceRangeStart)
                    seedEnd = targetRangeStart + (sourceRangeEnd-1 - sourceRangeStart)
                    print("target start: {}, target end: {}".format(seedStart,seedEnd))  
                    print("remaining start: {}, remaining end: {}\n".format(remaining[len(remaining)-1][0], remaining[len(remaining)-1][1]))  
                    break
                elif seedStart < sourceRangeStart and seedEnd > sourceRangeStart and seedEnd <= sourceRangeEnd:
                    #The whole range is not in the mapped range, need to split it, extra is on the left 
                    print("source start: {}, source end: {}".format(seedStart,seedEnd))
                    remaining.append((seedStart, sourceRangeStart-1))
                    seedStart = targetRangeStart + (sourceRangeStart - sourceRangeStart)
                    seedEnd = targetRangeStart + (seedEnd - sourceRangeStart)
                    print("target start: {}, target end: {}".format(seedStart,seedEnd))  
                    print("remaining start: {}, remaining end: {}\n".format(remaining[len(remaining)-1][0], remaining[len(remaining)-1][1]))  
                    break
                else:
                    #The whole range is not in the mapped range, check the other ranges
                    print("\n")
                

    #         for map in maps:
    #             for mapRanges in map:
    #                 if mappingNumber >= int(mapRanges[1]) and int(mappingNumber) < int(mapRanges[1])+int(mapRanges[2]):
    #                     rangeOffset = mappingNumber - int(mapRanges[1])
    #                     mappingNumber = int(mapRanges[0]) + rangeOffset
    #                     break
    #         locations.append(mappingNumber)    
    #     return min(locations) 
    
 
GetOptimizedPart2Answer()

#print("Part 1 Answer: " + str(GetPart1Answer()))
#print("Part 2 Answer: " + str(GetOptimizedPart2Answer()))
