
#Imports the random moudule to allow shuffling of the deck. 
import random

#Lists representing the suits and numbers of a standard deck of cards.  
Suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
Numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

#Class representing a single card in the deck. 
class card:
    def __init__(self, Number, Suit):
        #Initialize the card with a number (value) and a suit (e.g., 'Ace of Spades').
        self.Number = Number
        self.Suit = Suit

    #Display the card's calue and suit in a readable format. 
    def display(self):
        print(f"{self.Number} of {self.Suit}")

#Class representing the deck of cards. 
class Deck:
    def __init__(self):
         #Initialize the deck as an empty list.
        self.contents = []
        #Create the deck by generating all combinations of numbers and suits.
        self.contents = [card(Number, Suit) for Number in Numbers for Suit in Suits]
        #Shuffle the deck to randomize the card order.
        random.shuffle(self.contents)

    #Remove and return the top card from the deck.
    def pop(self):
        return self.contents.pop()

#function to determin the calue of a given card. 
def card_value(card):
    #Face cards (Jack, Queen, King) are worth 10 points each. 
    if card.Number in ['Jack', 'Queen', 'King']:
        return 10
    #Aces are worth 11 points by default 
    elif card.Number == 'Ace':
        return 11
    #Number cards are worth their numerical value. 
    else:
        return int(card.Number)



#Creates a new deck of cards and initialize empty hands for the player and dealer. 
Deck = Deck()
Player_hand = []
Dealer_hand = []

#Main game loop to handle multiple rounds. 
while True:
    #Clear the player and dealer hand at the start of each round.
    Player_hand.clear()
    Dealer_hand.clear()

    #Deals two cards to both the player and the dealer. 
    Player_hand = [Deck.pop(), Deck.pop()]
    Dealer_hand = [Deck.pop(), Deck.pop()]

    # Game logic for the player's turn.
    while True:
        #Calculate the players and dealers score based on the cards in the current 'hand'{LIST}.
        Player_score = sum(card_value(card) for card in Player_hand)
        Dealer_score = sum(card_value(card) for card in Dealer_hand)

        #Displays the player's current hand and total score. 
        print("You have the following cards:")
        for card in Player_hand:
            card.display()
        print(f"That comes to a total of: {Player_score}")

        #Asks the player if they want another card. 
        Choice = input('Do you want another card? (Yes or No): ')

        #If the player wants another card, draw one and add it to their hand. 
        if Choice.lower() == 'yes':
            New_card = Deck.pop()
            Player_hand.append(New_card)
        #if the player declines, end their turn. 
        elif Choice.lower() == 'no':
            break
        else:
            print("That's not an option. Let's try again, pick Yes or No.")
            continue

    #Dealer's turn: Keep drawing cards until the dealer's score is at least 17. 
    while Dealer_score < 17:
        New_card = Deck.pop()
        Dealer_hand.append(New_card)
        Dealer_score += card_value(New_card)

    #Display the dealer's final hand and score 
    print("The dealer has:")
    for card in Dealer_hand:
        card.display()
    print(f"Which gives them a score of {Dealer_score}.\n")

    #Determin the outcome of the round based on the scores. 
    if Player_score > 21: 
        print(f"The dealer has {Dealer_score}.")
        print("You have the following cards:")
        for card in Player_hand:
            card.display()
        print(f"Which gives you a score of {Player_score}.\n")
        print(f'The dealer has won as your hand exceeded 21.')
    elif Dealer_score > 21:
        print(f"The dealer has {Dealer_score}.")
        print("You have the following cards:")
        for card in Player_hand:
            card.display()
        print(f"Which gives you a score of {Player_score}.\n")
        print("You have won as the dealer's hand exceeds 21. Congratulations.")
    elif Player_score > Dealer_score:
        print(f"The dealer has {Dealer_score}.")
        print("You have the following cards:")
        for card in Player_hand:
            card.display()
        print(f"Which gives you a score of {Player_score}.\n")
        print("Congratulations, you have won.")
    elif Dealer_score > Player_score:
        print(f"The dealer has {Dealer_score}.")
        print("You have the following cards:")
        for card in Player_hand:
            card.display()
        print(f"Which gives you a score of {Player_score}.\n")
        print("Unfortunately, the dealer has won this hand.")
    else:
        print(f"The dealer has {Dealer_score}.")
        print("You have the following cards:")
        for card in Player_hand:
            card.display()
        print(f"Which gives you a score of {Player_score}.\n")
        print("It's a tie!!")

    #Ask the player if they want to play another round. 
    play_again = input("Do you want to play again? (Yes or No): ")
    if play_again.lower() != 'yes':
        break
#Thank the player for participating 
print("Thank you for playing!")








