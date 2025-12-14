logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random

def DealCard(Hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = cards[random.randint(0,len(cards)-1)]
    if card == 11:
        if sum(Hand) + 11 > 21:
            Hand.append(1)
        else:
            Hand.append(card)
    else:
        Hand.append(card)
    return Hand

def Game(PC, CC):

    if sum(PC) > 21:
        print("Busted, You Loose")
        return [PC, CC]
    elif sum(CC) > 21:
        print("Dealer got Busted")
        print("You Win")
        return [PC, CC]
    else:
        Choice = int(input("1: Hit, 2: Stand"))
        if Choice == 1:
            if sum(CC) <= 10:
                CC = DealCard(CC)
            PC = DealCard(PC)
            print(f"Your cards: {PC}")
            [PC, CC] = Game(PC, CC)
        elif Choice == 2:
            if sum(CC) <= 10:
                CC = DealCard(CC)
            if sum(PC) > sum(CC):
                print("You Win")
            elif sum(PC) < sum(CC):
                print("You Loose")
            elif sum(PC) == sum(CC):
                print("Draw")
    return [PC, CC]


PC = []
CC = []
input("Start game")
PC = DealCard(PC)
PC = DealCard(PC)
CC = DealCard(CC)
CC = DealCard(CC)



print(f"Your cards: {PC}")
print(f"Computers 1st card is: {CC[0]}")
[PC, CC] = Game(PC, CC)
print(f"Your final score is: {sum(PC)}, Dealers final score is: {sum(CC)}")





