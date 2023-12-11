import Order

class Limit:
    def __init__(self, price):
        self.price = price
        self.head = None
        self.tail = None

    def add_order(self, order):
        if not self.head:
            self.head = order
            self.tail = order

        else:
            self.tail.next_order = order
            order.prev_order = self.tail
            self.tail = order


    def remove_order(self):
        if not self.head:
            raise ValueError("Cannot remove order from empty list")

        temp_order = self.head

        self.head = self.head.next

        if self.head:
            self.head.prev = None
        else:
            self.tail = None

        return temp_order

    def __str__(self):
        return f"Limit(price = {self.price}, orders = {list(self)})"

    def __iter__(self):
        order = self.head
        while order:
            yield order
            order = order.next

