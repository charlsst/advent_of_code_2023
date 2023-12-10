import time

cardsFile = open("Day7/202307cards.txt")

fiveOfAKinds = []
fourOfAKinds = []
fullHouses = []
threeOfAKinds = []
twoPairs = []
onePairs = []
highs = []

weights = {"2" : 0, "3" : 1, "4" : 2, "5" : 3, "6" : 4, "7" : 5, "8" : 6, "9" : 7, "T" : 8, "J" : 9, "Q" : 10, "K" : 11, "A" : 12}
weights2 = {"2" : 1, "3" : 2, "4" : 3, "5" : 4, "6" : 5, "7" : 6, "8" : 7, "9" : 8, "T" : 9, "J" : 0, "Q" : 10, "K" : 11, "A" : 12}

doFirst = False

def insertIntoTable(valToInsertTable, tableToInsertInto):
    valToInsert = valToInsertTable[0]
    if len(tableToInsertInto) == 0 :
        #print("\nAppending to Table")
        tableToInsertInto.append(valToInsertTable)
        return tableToInsertInto
    else :
        #print("\nComparing")
        tableIndex = 0
        for val in tableToInsertInto :
            if valToInsert == val[0] : 
                tableToInsertInto.insert(tableIndex, valToInsertTable)
                return tableToInsertInto
            index = 0
            while index <= 4 :
                if not doFirst: #if doing part 2
                    #print(f"Vals: {weights[valToInsert[index]]} {weights[val[0][index]]}")
                    if weights2[valToInsert[index]] > weights2[val[0][index]] :
                        print(tableIndex, valToInsert)
                        tableToInsertInto.insert(tableIndex, valToInsertTable)
                        return tableToInsertInto
                    if weights2[valToInsert[index]] < weights2[val[0][index]] : break
                    index += 1
                else :
                    #print(f"Vals: {weights[valToInsert[index]]} {weights[val[0][index]]}")
                    if weights[valToInsert[index]] > weights[val[0][index]] :
                        print(tableIndex, valToInsert)
                        tableToInsertInto.insert(tableIndex, valToInsertTable)
                        return tableToInsertInto
                    if weights[valToInsert[index]] < weights[val[0][index]] : break
                    index += 1
            tableIndex += 1
    tableToInsertInto.append(valToInsertTable)
    return tableToInsertInto

cardsLines = cardsFile.readlines()
testVal = 1

for line in cardsLines:
    cardDict = {"2" : 0, "3" : 0, "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0, "T" : 0, "J" : 0, "Q" : 0, "K" : 0, "A" : 0}
    duos, trios, quads, quints = [], [], [], []
    game = line.strip().split(" ")

    for card in game[0] :
        if not doFirst :
            cardDict[card] += 1
            if card == "J" :
                if cardDict[card] > 1 and card not in duos : duos.append(card)
                if cardDict[card] > 2 and card not in trios : trios.append(card)
                if cardDict[card] > 3 and card not in quads : quads.append(card)
                if cardDict[card] > 4 and card not in quints : quints.append(card)
            else :
                if cardDict[card]+cardDict["J"] > 1 and card not in duos : duos.append(card)
                if cardDict[card]+cardDict["J"] > 2 and card not in trios : trios.append(card)
                if cardDict[card]+cardDict["J"] > 3 and card not in quads : quads.append(card)
                if cardDict[card]+cardDict["J"] > 4 and card not in quints : quints.append(card)
        else :
            cardDict[card] += 1
            if cardDict[card] > 1 and card not in duos : duos.append(card)
            if cardDict[card] > 2 and card not in trios : trios.append(card)
            if cardDict[card] > 3 and card not in quads : quads.append(card)
            if cardDict[card] > 4 and card not in quints : quints.append(card)

    print(f"Duos: {duos}, Trios: {trios}, Quads: {quads}, Quints: {quints}")
    time.sleep(1)

    if len(quints) >= 1 : fiveOfAKinds = insertIntoTable(game, fiveOfAKinds)
    elif len(quads) >= 1 : fourOfAKinds = insertIntoTable(game, fourOfAKinds)
    elif len(trios) >= 1 and len(duos) >= 2 : fullHouses = insertIntoTable(game, fullHouses)
    elif len(trios) >= 1 : threeOfAKinds = insertIntoTable(game, threeOfAKinds)
    elif len(duos) >= 2 : twoPairs = insertIntoTable(game, twoPairs)
    elif len(duos) >= 1 : onePairs = insertIntoTable(game, onePairs)
    else : highs = insertIntoTable(game, highs)

    testVal +=1

testVal = 0

fullTable = []
for val in fiveOfAKinds :
    fullTable.append(val)
    testVal += 1
for val in fourOfAKinds :
    fullTable.append(val)
    testVal += 1
print(len(fullTable))
for val in fullHouses :
    fullTable.append(val)
    testVal += 1
print(len(fullTable))
for val in threeOfAKinds :
    fullTable.append(val)
    testVal += 1
print(len(fullTable))
for val in twoPairs : 
    fullTable.append(val)
    testVal += 1
print(len(fullTable))
for val in onePairs :
    fullTable.append(val)
    testVal += 1
print(len(fullTable))
for val in highs :
    fullTable.append(val)
    testVal += 1

print(fullTable)
print(f"TestVal: {testVal}")

fullIndex = 0
total1 = 0

for card in fullTable :
    #print(f"EndTimes: {int(card[1])} * {(len(fullTable)-fullTable.index(card))} = {int(card[1]) * (len(fullTable)-fullTable.index(card))}")
    total1 += int(card[1]) * (len(fullTable)-fullTable.index(card))

print(f"Total (part 1): {total1}")

cardsFile.close()