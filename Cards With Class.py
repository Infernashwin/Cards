import random
class Card():
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

    def get_name(self):
        return self.rank

    def get_value(self):
        return self.value

    def show_card(self, msg):
        print(f"{msg}\nRank: {self.rank}, Suit: {self.suit}")

class Card_Deck():
    def __init__(self, suit_tuple, rank_tuple):
        self.deck = []
        for suit in suit_tuple:
            for value, rank in enumerate(rank_tuple, start = 1):
                card = Card(rank, suit, value)
                self.deck.append(card)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def get_card(self):
        card = self.deck[0]
        self.deck.pop(0)
        return card

def main():
    score = 50
    suit_tuple = ("Spades", "Hearts", "Clubs","Diamonds")
    rank_tuple = ("Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King")  
    deck_in_play = Card_Deck(suit_tuple, rank_tuple)
    play = True
    while play:
        deck_in_play.shuffle_deck()
        card = deck_in_play.get_card()
        for i in range(8):
            card.show_card("The Comparison Card is:")
            guess = input("Higher or Lower? [H/L]: ")
            card_in_play = deck_in_play.get_card()
            card_in_play.show_card("The Card Drew is:")
            if card_in_play.get_value() > card.get_value() and guess == "H" or card_in_play.get_value() < card.get_value() and guess == "L":
                print("Your Guess Was Correct")
                print("You earned 20 points")
                score += 20
            else:
                print("Your Guess Was Wrong")
                print("You Lost 15 Points")
                score -= 15
            print(f"Your Current Score is {score}")
        play = input("Would you like to play again? [Y/N]: ") == "Y"
        score = deck_in_play.get_score()
        deck_in_play = Card_Deck(suit_tuple, rank_tuple)
    print("Game Is Over")

main()   