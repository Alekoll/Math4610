
from PythonLearn import Card
from PythonLearn import Deck

def Display(inputList):
    for i in range(len(inputList)):
        print(inputList[i].getValue(), " of ",inputList[i].getMano(), " ",inputList[i].getCoin())

def SortId(inputList):
    for i in range(len(inputList) - 1):
        currMinIndex = i

        for j in range(i + 1, len(inputList)):
            if inputList[currMinIndex].getId() > inputList[j].getId():
                currMinIndex = j

        if currMinIndex != i:
            inputList[i], inputList[currMinIndex] = inputList[currMinIndex], inputList[i]

def SortValue(inputList):
    for i in range(len(inputList) - 1):
        currMinIndex = i

        for j in range(i + 1, len(inputList)):
            if inputList[currMinIndex].getValue() > inputList[j].getValue():
                currMinIndex = j

        if currMinIndex != i:
            inputList[i], inputList[currMinIndex] = inputList[currMinIndex], inputList[i]

def search(input_list, key):
    
    low = 0
    high = len(input_list) - 1
    while high >= low:
        
        mid = (high + low) // 2
        if key == input_list[mid].getUnId():
            return True
        elif key < input_list[mid].getUnId():
            high = mid - 1
        else:
            low = mid + 1

    return False

def getHand(cardValue, cardMano, cardCoin):
    mano = ["Rock", "Paper", "Scissors"]
    coin = ["Heads", "Tails"]
    inte = int(cardValue)
    handValue = 2 * ((inte - 1) + (20 * mano.index(cardMano)) + coin.index(cardCoin))
    return handValue
    
def Menu(aList,aDeck):
    print("Hello, Welcome To Gubbins", "Type in what you want to do.", "Sort by Id", "Sort by Value", "Find card", "New Card", "Quit", sep='\n')
    string = input()

    if(string == "Sort by Id"):
        SortId(aList)
        Display(aList)
        
            
    if(string == "Sort by Value"):
        SortValue(aList)
        Display(aList)
        

    if(string == "Find card"):
       
        cardvalue = input("CardValue")
        cardMano = input("Mano")
        cardCoin = input("Coin")
        hand = getHand(cardvalue, cardMano, cardCoin)
        if(search(aList, hand) is True):
            print("Card is in Hand")
        else:
            print("Card is not in hand")


    if(string == "New card"):
        aDeck.shuffle(aList)
        del aList[:]
        for i in range(30):
            aList.append(aDeck)
    
    if(string == "Quit"):
        return True
    return False
        
        


def main():
    hand = []
    deck = Deck()

    for i in range(30):
        hand.append(deck.draw())
    isTrue = False

    while(isTrue is not True):
        isTrue = Menu(hand, deck)

        
            
    
main()
    
    