import random
import os

deck = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]*4
Dealerhand = []
Playerhand = []
Players = []

def Deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand

def Total(hand):
    total = 0
    for card in hand:
        if card == "J":
            total += 10

        elif card == "Q":
            total += 10

        elif card == "K":
            total += 10

        elif card == "A":
            if total >= 11:
                total += 1

            else: total += 11
        else: total += int(card)
    return total

def checkBlackjack(hand, hand2):
    blackjack = 0
    if Total(hand) == 21:
        blackjack = 1

        if Total(hand2) == 21:
            blackjack = 3

    elif Total(hand2) == 21:
        blackjack = 2

    else: blackjack = 0
    return blackjack

def checkBust(hand):
    if Total(hand) > 21:
        return True
    else: return False

def hit(hand):
    card = deck.pop()
    hand.append(card)

def resetDecks(deck):
    deck = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]*4
    return deck

def playAgain():
    again = input("Do you want to play again? (Y/N) : ")
    if again == "y":
        game()

    else:
        print("Bye!\n")
        exit()

def clear():
    print("Clear!\n")
    if os.name =='nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def game():
    choice = 0
    clear()
    resetDecks(deck)
    print("Welcome to Blackjack \n")
    Dealerhand = Deal(deck)
    Playerhand = Deal(deck)
    print("Your hands hand is : "+ str(Playerhand[0]) +" and "+ str(Playerhand[1]) + " which totals to " + str(Total(Playerhand)) + "\n Dealers first card is: " + str(Dealerhand[0])+"\n")

    #check surrender, split and everything else if you even can be assed to implement 
    blackjackCheckedResult = checkBlackjack(Playerhand, Dealerhand)
    if blackjackCheckedResult == 1:
        print("You have a blackjack and dealer's second card is : "+ str(Dealerhand[-1])+" so you WIN!\n")
        playAgain()

    elif blackjackCheckedResult == 2:
        while checkBust(Playerhand)!=True:
            choice = input("Choose to hit or stand\n")

            if choice == "hit":
                hit(Playerhand)
                print("\nYou got " + str(Playerhand[-1]) + "and totals to "+ str(Total(Playerhand)) + "!\n")

                if checkBust(Playerhand) == True:
                    print("Player Bust!\n")
                    playAgain()

            elif choice == "stand":
                print("Dealer's second card is: " + str(Dealerhand[1]) + " and Dealers hand totals to " + str(Total(Dealerhand)) + "!\n")
                print("Dealer has a blackjack! You LOOSE!\n")
                playAgain()
        
    elif blackjackCheckedResult == 3:
        print("Both Player and Dealer have a blackjack! It's a TIE!\n")
        playAgain()

    else: 
        print("No Blackjacks... at least yet.\n")

        while checkBust(Playerhand)!=True:
            choice = input("Choose to hit or stand\n")

            if choice == "hit":
                hit(Playerhand)
                print("You got " + str(Playerhand[-1]) + " and total to "+ str(Total(Playerhand)) + "!\n")

                if checkBust(Playerhand) == True:
                    print("Player Bust!\n")
                    playAgain()

            elif choice == "stand":
                print("Dealers second card is: " + str(Dealerhand[1]) + " and Dealers hand totals to " + str(Total(Dealerhand)) + "!\n")
                
                while Total(Dealerhand) < 17:
                    print("Since the Dealer totals to less than 17 the Dealer has to hit\n")
                    hit(Dealerhand)
                    print("Dealer got " + str(Dealerhand[-1]) + " and totals to "+ str(Total(Dealerhand)) + "!\n")

                    if checkBust(Dealerhand) == True:
                        print("Dealer Bust and You WIN\n")
                        playAgain()

                    elif Total(Dealerhand) > 17 and checkBust(Dealerhand) == False:
                        print("Dealer totals to more than 17 and will not hit anymore.\n")

                    elif Total(Dealerhand) == 17 and checkBust(Dealerhand == False):
                        print("Dealer totals to 17 and will not hit anymore.\n")

                if Total(Dealerhand) >= 17 and checkBust(Dealerhand) == False:

                    if Total(Playerhand) <= Total(Dealerhand):
                        print("Player totals to "+ str(Total(Playerhand))+ " and the Dealer totals to " + str(Total(Dealerhand)) + ". You loose!\n")
                        playAgain()

                    else:
                        print("Player totals to more than the Dealer. You Win!\n")
                        playAgain()

                

if __name__ == "__main__":
    while True:
        playercount = input("How many players want to play? (1-2)")
        try:
            val = int(playercount)

        except ValueError:
            print("Please enter a number between 1 and 2.")

        else:
            break
    pcount = int(playercount)
    if pcount == 1:
        game()

    elif pcount == 2:
        print("multiplayer not implemented yet lol")
        exit()

    else:
        print("multiplayer not implemented yet lol")
        exit()



