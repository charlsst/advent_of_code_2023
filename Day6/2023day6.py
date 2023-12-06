speedsFile = open("Day6/202306speeds.txt","r")

times = speedsFile.readline().strip().split()[1:]
distances = speedsFile.readline().strip().split()[1:]

combTime = "".join(times)
combDist = "".join(distances)

total1 = 0
for count in range(0, len(distances)):
    timeHeld = 0
    timeTravel = int(times[count])
    currentSpeed = 0
    numOfPoss = 0
    while timeHeld < int(times[count]) :
        distance = currentSpeed*timeTravel
        if distance > int(distances[count]) :
            numOfPoss += 1
        timeHeld += 1
        timeTravel -= 1
        currentSpeed += 1
    if total1 == 0 : total1 = numOfPoss
    else : total1 *= numOfPoss
print(f"Part 1: {total1}")

total2 = 0
timeHeld = 0
timeTravel = int(combTime)
currentSpeed = 0
numOfPoss = 0
while timeHeld < int(combTime) :
    distance = currentSpeed*timeTravel
    if distance > int(combDist) :
        numOfPoss += 1
    timeHeld += 1
    timeTravel -= 1
    currentSpeed += 1
if total2 == 0 : total2 = numOfPoss
else : total2 *= numOfPoss
print(f"Part 2: {total2}")

speedsFile.close()