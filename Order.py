class Order:
    """
    Order Class with key: Price and Values: Type, Suit, Owner)

    Type can take on values 0 or 1 where 0 is buy and 1 is sell
    Suit can take on values from [0,3] where 0 is Spades, 1 is Clubs, 2 is Diamonds and 3 is Hearts
    Owner can take on values from [0,3] where each number corresponds to a Trader ID
    """
    self.price = 0
    self.type = 0
    self.suit = 0
    self.owner = 0

    def __init__(self, data):
        self.price = data[0]
        self.type = data[1]
        self.suit = data[2]
        self.owner = data[3]

    def get_price(self):
        return self.price

    def get_type(self):
        return self.type

    def get_suit(self):
        return self.suit

    def get_owner(self):
        return self.owner

