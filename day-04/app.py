inputFile = open("input.txt", "r")
cards = inputFile.readlines()
inputFile.close()

def GetPart1Answer():
    sum = 0
    for card in cards:
        card = card.split(':')[1].split("\n")[0]
        winningCard = card.split('|')[0].split(" ")
        myCard = card.split('|')[1].split(" ")
        while ("" in winningCard):
            winningCard.remove("")
        while ("" in myCard):
            myCard.remove("")

        gameScore = 0
        for myNum in myCard:
            if winningCard.__contains__(myNum):
                if gameScore == 0:
                    gameScore = 1
                else:
                    gameScore = gameScore * 2
        sum = sum + gameScore
    return sum

def GetCards():
    winningCards = []
    myCards = []
    winningCard = ""
    myCard = ""
    for card in cards:
        card = card.split(':')[1].split("\n")[0]
        winningCard = card.split('|')[0].split(" ")
        myCard = card.split('|')[1].split(" ")
        while ("" in winningCard):
            winningCard.remove("")
            winningCards.append(winningCard)
        while ("" in myCard):
            myCard.remove("")
            myCards.append(myCard)

    return (winningCards, myCards)

def ProcessCards(cards):
    sum = 0
    while (len(cards) > 0):
        cardID = 0
        winNum = 0
        cardCopies = []
        for card in cards:
            winCard = card[0]
            myCard = card[1]
            for n in myCard:
                if winCard.__contains__(n):
                    winNum = winNum + 1
                    cardCopies.append((card, cardID + winNum))    
                    sum = sum + 1
        cards = cardCopies[0]
    return sum

def GetPart2Answer():
    ProcessCards(GetCards())
    # sum = 0
    # cardID = 0
    # winNum = 0
    # cardCopies = []
    # for card in GetCards():
    #     winCard = card[0]
    #     myCard = card[1]
    #     for n in myCard:
    #         if winCard.__contains__(n):
    #             winNum = winNum + 1
    #             cardCopies.append((card, cardID + winNum))    
    #     cardID = cardID + 1

#print(GetPart2Answer()) 
print("Part 1 Answer: " + str(GetPart1Answer()))

















    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
