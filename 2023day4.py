bingo = open("AdventOfCode/202304bingo.txt")

total = 0
index = 0

amountOfCards = []
for count in range(0, 187) : amountOfCards.append(1)

for card in bingo.readlines() :
    index += 1
    winners = set()
    numbers = set()

    cardTable = card.split("|")
    cardTable[0] = cardTable[0].split(" ")
    cardTable[0] = cardTable[0][2:]
    for val in cardTable[0]:
        if val == '' : cardTable[0].remove(val)
    
    cardTable[1] = cardTable[1].split(" ")
    for val in cardTable[1]:
        if val == '' : cardTable[1].remove(val)

    for val in cardTable[0] : winners.add(val.strip())
    for val in cardTable[1] : numbers.add(val.strip())

    results = winners & numbers
    numOfNewCards = len(results)
    print(f"Set {index} has {numOfNewCards} wins")

    for count in range(index, index+numOfNewCards) :
        if count < 187 :
            amountOfCards[count] += amountOfCards[index-1]

    if len(results) > 0 :
        total += 2**(len(results)-1)

print(f"Total: {total}")
totalCardAmount = 0

print(amountOfCards)

for num in amountOfCards :
    totalCardAmount += num
print(totalCardAmount)

bingo.close()
