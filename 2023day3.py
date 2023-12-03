schematic = open("AdventOfCode/202303schematic.txt")

sTable= []
gears = []
totalSum = 0
totalSum2 = 0

def findNumber(posX, line):
    digit = line[posX]
    number = ""
    while digit.isdigit() :
        posX -= 1
        if posX < 0 : break
        digit = line[posX]
    
    posX += 1
    digit = line[posX]
    while digit.isdigit() :
        number += digit
        posX += 1
        if posX >= len(line) : break
        digit = str(line[posX])
    
    #print(f"Number: {number}")
    
    return int(number)


for line in schematic.readlines() :
    sTable.append(line.strip())

indexY = 0

for line in sTable:
    #print(f"Y: {indexY}")

    indexX = 0
    while indexX < len(line) :

        if sTable[indexY][indexX].isdigit() and sTable[indexY][indexX] != "." :
            for count in range(0,8) :
                if count == 0 : nbX, nbY = indexX-1, indexY-1
                elif count == 1 : nbX, nbY = indexX, indexY-1
                elif count == 2 : nbX, nbY = indexX+1, indexY-1
                elif count == 3 : nbX, nbY = indexX-1, indexY
                elif count == 4 : nbX, nbY = indexX+1, indexY
                elif count == 5 : nbX, nbY = indexX-1, indexY+1
                elif count == 6 : nbX, nbY = indexX, indexY+1
                elif count == 7 : nbX, nbY = indexX+1, indexY+1

                if nbX > 0 and nbY > 0 and  nbY +1 < len(sTable) and nbX < len(line) :
                    neighbour = sTable[nbY][nbX]
                    #print(f"Neighbour: {neighbour} ({nbX}, {nbY}) of Number: {sTable[indexY][indexX]} ({indexX}, {indexY})")
                    if not neighbour.isdigit() and neighbour != "." :
                        newNum = findNumber(indexX, line)
                        totalSum += newNum
                        product = 0
                        if neighbour == "*" :
                            for gear in gears :
                                gearTab = gear.split(".")
                                #print(nbX, gearTab[0], nbY, gearTab[1], int(gearTab[2]) * newNum)
                                if int(nbX) == int(gearTab[0]) and int(nbY) == int(gearTab[1]) :
                                    product = int(gearTab[2]) * newNum
                                    totalSum2 += product
                            gears.append(f"{nbX}.{nbY}.{newNum}")

                        while sTable[indexY][indexX].isdigit() and sTable[indexY][indexX] != "." :
                            if indexX+1 < len(line) : indexX += 1
                            else : break
                        break
        indexX += 1

    indexY += 1

print(f"Part 1 Total: {totalSum}")
print(f"Part 2 Total: {totalSum2}")

schematic.close()
