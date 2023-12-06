import math
seedsFile = open("Day5/202305seeds.txt","r")

class Seed():
    def __init__(self, seedId):
        self.seedId = seedId
        self.soilId = seedId
        self.fertilizerId = seedId
        self.waterId = seedId
        self.lightId = seedId
        self.temperatureId = seedId
        self.humidityId = seedId
        self.locationId = seedId
    
    def __str__(self): return f"{self.seedId} - {self.soilId} - {self.fertilizerId} - {self.waterId} - {self.lightId} - {self.temperatureId} - {self.humidityId} - {self.locationId}"

seedsText = seedsFile.readline().strip().split(" ")[1:]
seedsFile.readline()
seedsFile.readline()

def createConnectionTable():
    connectionTable = []
    line = seedsFile.readline().strip()
    while line != "" :
        connectionTable.append(line)
        line = seedsFile.readline().strip()
    seedsFile.readline()

    return connectionTable

seeds = []

for seed in seedsText: seeds.append(Seed(seed))

seedToSoil = createConnectionTable()
soilToFert = createConnectionTable()
fertToWater = createConnectionTable()
waterToLight = createConnectionTable()
lightToTemp = createConnectionTable()
tempToHum = createConnectionTable()
humToLoc = createConnectionTable()

def assignValue(tableToCheck, valToCheck):
    valToCheck = int(valToCheck)
    for i in tableToCheck :
        line = i.split(" ")
        if valToCheck >= int(line[1]) and valToCheck <= int(line[1])+int(line[2]) :
            #print(f"Value to check {valToCheck} is between {int(line[1])} and {int(line[1])+int(line[2])}")
            #print(f"VAL: {(valToCheck-int(line[0]))} + {int(line[1])} ({int(line[2])}) = {valToCheck-int(line[0]) + int(line[1])}")
            return (valToCheck-int(line[1])) + int(line[0])
    return valToCheck

def reverseValue(tableToCheck, valToCheck):
    valToCheck = int(valToCheck)
    for i in tableToCheck :
        line = i.split(" ")
        if valToCheck >= int(line[0]) and valToCheck <= int(line[0])+int(line[2]) :
            #print(f"Value to check {valToCheck} is between {int(line[1])} and {int(line[1])+int(line[2])}")
            #print(f"VAL: {(valToCheck-int(line[0]))} + {int(line[1])} ({int(line[2])}) = {valToCheck-int(line[0]) + int(line[1])}")
            return (valToCheck-int(line[0])) + int(line[1])
    return valToCheck

lowestVal = 1000000000000000
for seed in seeds :
    seed.soilId= assignValue(seedToSoil, seed.seedId)
    seed.fertilizerId = assignValue(soilToFert, seed.soilId)
    seed.waterId = assignValue(fertToWater, seed.fertilizerId)
    seed.lightId = assignValue(waterToLight, seed.waterId)
    seed.temperatureId = assignValue(lightToTemp, seed.lightId)
    seed.humidityId = assignValue(tempToHum, seed.temperatureId)
    seed.locationId = assignValue(humToLoc, seed.humidityId)

    if seed.locationId < int(lowestVal) :
        lowestVal = seed.locationId

print(f"Lowest Val (part 1): {lowestVal}")

minLoc = 13630381
found = False

print("Time to wait 3 hours! Get your popcorn ready!")

minLoc = 0
while not found :
    val = reverseValue(humToLoc, minLoc)
    val = reverseValue(tempToHum, val)
    val = reverseValue(lightToTemp, val)
    val = reverseValue(waterToLight, val)
    val = reverseValue(fertToWater, val)
    val = reverseValue(soilToFert, val)
    val = reverseValue(seedToSoil, val)

    for count in range(0, len(seedsText), 2):

        if val >= int(seedsText[count]) and val <= int(seedsText[count])+int(seedsText[count+1]):
            found = True
            print(f"Min Val ATM: {minLoc} for seed {val}")
            break

    minLoc += 1

print(f"Lowest Val (part 2): {minLoc}")

seedsFile.close()