import random
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def get_card(deck):
    card = deck[0]
    deck.pop(0)
    return card

def main(): 
    suit_tuple = ("Spades", "Hearts", "Clubs","Diamonds")
    rank_tuple = ("Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King")
    deck = []
    for suit in suit_tuple:
        for value, rank in enumerate(rank_tuple, start = 1):
            card = {"rank":rank, "suit":suit, "value":value}
            deck.append(card)  
    score = 50
    play = True
    while play:
        deck_in_play = shuffle_deck(deck)
        look = get_card(deck_in_play)
        print(f"Your current card is {look}")
        for i in range(8):
            card_in_play = get_card(deck_in_play)
            guess = input("Higher or Lower? [H/L]: ")
            print(f"The card was {card_in_play}")
            if card_in_play["value"] > look["value"] and guess == "H" or card_in_play["value"] < look["value"] and guess == "L":
                print("Your Guess Was Correct")
                print("You earned 20 points")
                score += 20
            else:
                print("Your Guess Was Wrong")
                print("You Lost 15 Points")
                score -= 15
            print(f"Your Current Score is {score}")
        play = input("Would you like to play again? [Y/N]: ") == "Y"
    print("Game Is Over")
main()