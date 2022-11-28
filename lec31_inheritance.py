import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
        
    def __str__(self):
        """ () -> str
        >>> card = Card("Hearts", "Ten")
        >>> print(card)
        Ten of Hearts

        """
    
        #return self.rank + " of " + self.suit
        
        # f string => special about python
        # {a} automaticaly convert any a variable into a str
        return f"{self.rank} of {self.suit}"
    
    
class Deck:
    def __init__(self):
        self.cards = []
        # self.cards.append(Card("Hearts", "Two")) do that for everycard is very unefficient
        
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]:
                card = Card(suit,rank)
                self.cards.append(card)
                
    def __str__(self):
        s = ''
        for card in self.cards:
            s += str(card) + '\n'
        return s.strip()
    
    def add_card(self, card):
        if type(card) != Card:
            raise ValueError("Must add a Card object")
        self.cards.append(card)
        
    def pop_card(self):
        return self.cards.pop() # Returning the last elements, -1 by default
    
    
    def shuffle(self):
        # Does not return anything
        random.shuffle(self.cards)
        
    def deal_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
        
        
# inheritance
# You have two different classes => they do very similar things
# They are not exactly the same

# For example we dont want 52 cards in our hand
# You want to compare two hands but not two decks

# The Hand Class will inherit from the Deck class
# The Hand Class is the child class/subclass and the Deck is the parent class/superclass
class Hand(Deck):
    """ Represents a hand of playing cards."""
    
    def __init__(self, label): # Overwritting the construction methods
        self.cards = []
        self.label = label
        
        
    def __str__(self):
        s = 'Label : ' + self.label + '\nCards:\n'
        return s + super().__str__()
        
        #for card in self.cards:
        #    s += str(card) + '\n'
        #return s.strip()
        
    