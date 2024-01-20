class Card:
    
    def __init__(self, id, winNumbers, ownNumbers):
        self.id = id
        self.winNumbers = winNumbers
        self.ownNumbers = ownNumbers
        self.wonCards = []
    
    def GetWinAmt(self):
        winAmt = 0
        for num in self.ownNumbers:
            if self.winNumbers.__contains__(num):
                winAmt += 1
        return winAmt
######################################################

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

######################################################

def GetPart1Answer():
    sum = 0
    for card in lines:
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
########################################################

def ParseInput():
    cards = []
    for line in lines:
        id = line.split(':')[0].strip("Card ")
        card = line.split(':')[1].split("\n")[0]
        winningCard = card.split('|')[0].split(" ")
        myCard = card.split('|')[1].split(" ")
        
        while ("" in winningCard):
            winningCard.remove("")
        while ("" in myCard):
            myCard.remove("")
        
        newCard = Card(int(id), winningCard, myCard)
        cards.append(newCard)    
    return cards


allCards = ParseInput()

# for card in allCards:
#     for i in range(card.id+1, card.id+card.GetWinAmt()+1):
#         card.wonCards.append(allCards[i-1])
#     print("\n")

sum = 0
def GetWins(cards):
    global sum
    for card in cards:
        if card.GetWinAmt() > 0:
            #sum += card.GetWinAmt()
            for i in range(card.id+1, card.id+1 + card.GetWinAmt()):
                card.wonCards.append(allCards[i-1])
                sum += 1
                #print("Card " + str(card.id) + ": " + str(card.winNumbers) + " | " + str(card.ownNumbers))
            GetWins(card.wonCards)
                #for wonCard in card.wonCards:
                    #print(str(wonCard.id) + ": " + str(wonCard.winNumbers) + " | " + str(wonCard.ownNumbers))
                #print("\n")


GetWins(allCards)

print(sum)

#def GetPart2Answer():
    



#print("Part 1 Answer: " + str(GetPart1Answer()))

















    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    # Card 6: 3t 18 13 56 72 | 74 77 10 23 35 67 36 11
