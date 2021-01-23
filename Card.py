#class call card
class Card:
    #define method init
    def __init__(self,rank,suit):
        #assign values
        self.rank = rank
        self.suit = suit
    #define method getRank to return the rank of cards
    def getRank(self):
        return self.rank
    #define method getRank to return the suit of cards
    def getSuit(self):
        return self.suit
    #define method value to return the value of cards
    def value(self):
        self.score = 0
        #if the card is 1-10 then assign the value as the rank
        if self.rank > 0 and self.rank < 11:
            self.score = self.rank
        #if the card is with face then assign the value as 10
        elif self.rank==11 or self.rank==12 or self.rank==13:
            self.score = 10
        #else print out the error message
        else:
            print("Rank should be between 1 and 13 inclusive.")
        #return the value of cards
        return self.score
    #define method str
    def __str__(self):
        #assign cards scores according to their rank
        if self.rank == 1:
            self.score = "One"
        elif self.rank == 2:
            self.score = "Two"
        elif self.rank == 3:
            self.score = "Three"
        elif self.rank == 4:
            self.score = "Four"
        elif self.rank == 5:
            self.score = "Five"
        elif self.rank == 6:
            self.score = "Six"
        elif self.rank == 7:
            self.score = "Seven"
        elif self.rank == 8:
            self.score = "Eight"
        elif self.rank == 9:
            self.score = "Nine"
        elif self.rank == 10:
            self.score = "Ten"
        elif self.rank == 11:
            self.score = "Jack"
        elif self.rank == 12:
            self.score = "Queen"
        elif self.rank == 13:
            self.score = "King"

        #assign cards full name to print, according to their initial
        if self.suit == "d":
            self.suit = "Diamonds"
        elif self.suit == "c":
            self.suit = "Clubs"
        elif self.suit == "h":
            self.suit = "Hearts"
        elif self.suit == "s":
            self.suit = "Spades"
        #return the cards information
        return str(self.score) + " of " + str(self.suit)
