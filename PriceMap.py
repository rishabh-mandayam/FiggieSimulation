import Order
from collections import defaultdict

class PriceMap:
    """
    PriceMap Class implemented as a Hashmap of Queues

    Each Queue is keyed using a limit price and contains Order instances
    Each Order instance has the same price as the corresponding queue
    """

    def __init__(self):
        self.data = defaultdict(list)
        self.min_price = None
        self.max_price = None

    def insert(self, order):
        assert order.get_price() >= 0
        price = order.get_price()

        if self.min_price is None or price < self.min_price:
            self.min_price = price

        if self.max_price is None or price < self.max_price:
            self.max_price = price

        limit = self.data[price]

        limit.append(order)

    def get_min(self):
        if self.min_price is None:
            raise ValueError("PriceMap is Empty!")

        return self.data[self.min_price][0]

    def get_max(self):
        if self.max_price is None:
            raise ValueError("PriceMap is Empty!")

        return self.data[self.max_price][0]

    def extract_min(self):
        if self.min_price is None:
            raise ValueError("PriceMap is Empty!")

        min_order = self.data[self.min_price].pop(0)

        if len(self.data[self.min_price]) == 0:
            self.min_price = None

            for price in self.data:
                if self.min_price is None or price < self.min_price:
                    self.min_price = price

        return min_order

    def extract_min(self):
        if self.max_price is None:
            raise ValueError("PriceMap is Empty!")

        max_order = self.data[self.max_price].pop(0)

        if len(self.data[self.max_price]) == 0:
            self.max_price = None

            for price in self.data:
                if self.max_price is None or price < self.max_price:
                    self.max_price = price

        return max_order
