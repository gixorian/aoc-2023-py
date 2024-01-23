######################################################

from typing import assert_type


inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

######################################################

seeds = []
index = 0
maps = [[],[],[],[],[],[],[]]
s2s = []
s2f = []
f2w = []
w2l = []
l2t = []
t2h = []
h2l = []

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

print(min(locations))



#for m in maps:
#    for i in m:
#        print(i)
#    print("")
#print("")
