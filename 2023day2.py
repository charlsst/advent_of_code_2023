gamesFile = open("AdventOfCode/202302games.txt","r")
games = gamesFile.readlines()

maxRed = 12
maxGreen = 13
maxBlue = 14

totalScore = 0

doFirstOnly = False

for game in games :
    possible = True
    formattedGame = []
    formattedGame = game.replace(":",";").split(";")

    minRed = 0
    minGreen = 0
    minBlue = 0

    for section in formattedGame :
        subSections = section.strip().replace(",", " ").split(" ")
        index = 0
        for subSection in subSections :
            if not doFirstOnly :
                if subSection == "red" :
                    if int(subSections[index-1]) > minRed : minRed = int(subSections[index-1])
                if subSection == "green" :
                    if int(subSections[index-1]) > minGreen : minGreen = int(subSections[index-1])  
                if subSection == "blue" :
                    if int(subSections[index-1]) > minBlue : minBlue = int(subSections[index-1])   
            else :
                if subSection == "red" :
                    if int(subSections[index-1]) > maxRed : possible = False
                if subSection == "green" :
                    if int(subSections[index-1]) > maxGreen : possible = False
                if subSection == "blue" :
                    if int(subSections[index-1]) > maxBlue : possible = False
            index += 1
    
    if not doFirstOnly :
        totalScore += minRed*minGreen*minBlue
    elif possible :
        totalScore += int(formattedGame[0].split(" ")[1])

print(f"Final Score: {totalScore}")

gamesFile.close()
