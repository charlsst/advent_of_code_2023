stringsFile = open("Day1/202301strings.txt","r")
stringLines = stringsFile.readlines()

numbers = []
textNumbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

doFirstOnly = False #If True, only day one will be performed (consider only the integer numbers and not the strings)

for stringLine in stringLines:
    stringLine = str(stringLine).strip()
    indexStart = 0
    indexEnd = len(stringLine)-1

    firstNum = -1
    secondNum = -1

    firstNumStr = ""
    secondNumStr = ""

    firstFound = False
    secondFound = False

    for charInLine in stringLine :
        if charInLine.isdigit() :
            firstNum = int(charInLine)
            firstFound = True
            firstNumStr = ""
        else :
            if not doFirstOnly :
                firstNumStr += str(charInLine)
                for textNum in textNumbers :
                    if firstNumStr.replace(" ", "").find(str(textNum)) != -1 :
                        firstNum = textNumbers.index(textNum)
                        firstFound = True
        if firstFound : break

    for charInLine in stringLine[::-1] :
        if charInLine.isdigit() :
            secondNum = int(charInLine)
            secondFound = True
            secondNumStr = ""
        else :
            if not doFirstOnly :
                secondNumStr += str(charInLine)
                for textNum in textNumbers :
                    if str(secondNumStr[::-1].replace(" ", "")).find(str(textNum)) != -1 :
                        secondNum = textNumbers.index(textNum)
                        secondFound = True
        if secondFound : break


    if firstFound and secondFound :
        foundNumber = int(str(firstNum)+str(secondNum))
        numbers.append(foundNumber)
    # "fdfdf1ffsdf" == 11
    # "eighthree"
    print(foundNumber)
    
finalResult = 0
for number in numbers :
    finalResult += int(number)

print(finalResult)

stringsFile.close()
