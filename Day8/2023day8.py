import math

mapFile = open("Day8/202308map.txt","r")

class Mapper():
    def __init__(self, line):
        self.start = line[0:3]
        self.left = line[7:10]
        self.right = line[12:15]

directions = mapFile.readline()
mappedArray = {}
currentMappedTable = []
LCMTable = []

doFirst = False #CHANGE THIS TO DO PART 1

finished = False

directionIndex = 0
steps = 0

mapFile.readline()

line = mapFile.readline().strip()
while line != "" :
    pos = line[0:3]
    mappedArray[pos] = (Mapper(line))
    if not doFirst :
        if line[2] == "A" : currentMappedTable.append(pos)
    else:
        if line[0:3] == "AAA" : currentMappedTable.append(pos)
    line = mapFile.readline().strip()

while not finished or len(currentMappedTable) >= 1 :
    steps += 1

    index = 0
    for currentMapped in currentMappedTable :
        if directions[directionIndex] == "L" : currentMappedTable[currentMappedTable.index(currentMapped)] = mappedArray[currentMapped].left
        elif directions[directionIndex] == "R" : currentMappedTable[currentMappedTable.index(currentMapped)] = mappedArray[currentMapped].right
        else: print(f"{mappedArray[currentMapped].start} to {mappedArray[currentMapped].right} NOT POSSIBLE! (steps: {steps}) (direction_index: {directionIndex})")

    #print(f"{tempTable} to {currentMappedTable}")

    directionIndex += 1
    if directionIndex >= len(directions)-1 : directionIndex = 0
    #print(directions[0:directionIndex])
    
    tempIndex = 0
    for currentMapped in currentMappedTable :
        tempIndex += 1
        if not doFirst :
            if currentMapped[2] == "Z" :
                LCMTable.append(steps)
                currentMappedTable.remove(currentMapped)
                finished = True
            else :
                finished = False
                break
        else :
            if currentMapped == "ZZZ" : finished = True
            else :
                finished = False
                break
        if tempIndex >= 2 : print(f"{currentMappedTable} (steps: {steps})")

if not doFirst :
    index = 0
    steps = 1
    while index <= len(LCMTable)-1 :
        steps = math.lcm(steps, LCMTable[index])
        index += 1
print(f"It took {steps} steps!")

mapFile.close()