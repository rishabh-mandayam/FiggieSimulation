class Order:
    """
    Order Class with key: Price and Values: Type, Suit, Owner)

    Type can take on values 0 or 1 where 0 is buy and 1 is sell
    Suit can take on values from [0,3] where 0 is Spades, 1 is Clubs, 2 is Diamonds and 3 is Hearts
    Owner can take on values from [0,3] where each number corresponds to a Trader ID
    Volume is just the order volume, ie how much of asset j is being sold
    """
    self.order_id
    self.price = 0
    self.type = 0
    self.suit = 0
    self.owner = 0
    self.volume = 0

    def __init__(self, data, next_order = None, prev_order = None):
        self.price = data[0]
        self.type = data[1]
        self.suit = data[2]
        self.owner = data[3]
        self.volume = data[4]
        self.next_order = next_order
        self.prev_order = prev_order

    def get_price(self):
        return self.price

    def get_type(self):
        return self.type

    def get_suit(self):
        return self.suit

    def get_owner(self):
        return self.owner

    def get_volume(self):
        return self.volume

