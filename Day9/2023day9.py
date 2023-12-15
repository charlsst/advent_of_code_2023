sensorFile = open("Day9/202309oasisSensor.txt","r")

import time

sequences =  sensorFile.readlines()

total1 = 0
total2 = 0

for count in range(0, len(sequences)):
    sequenceTable = []

    sequence = sequences[count].strip().split(" ")
    sequenceTable.append(sequence)

    index = 0
    while int(("".join(sequence)).replace("-","")) != 0 :
        newSequence = []
        while index <= len(sequence)-2 :
            newSequence.append(str(int(sequence[index+1])-int(sequence[index])))
            index += 1
        sequenceTable.append(newSequence)
        sequence = newSequence
        index = 0

    sequenceTable.reverse()

    before = 0
    for seq in sequenceTable : before = int(seq[-1]) + before
    total1 += before

    after = 0
    for seq in sequenceTable : after = int(seq[0]) - after
    total2 += after

print(f"Total (part 1): {total1}\nTotal (part 2): {total2}")


sensorFile.close()