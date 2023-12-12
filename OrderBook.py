import Order
import PriceMap

class OrderBook:
    """
    OrderBook Class

    Contains 2 PriceMaps, one for buying and one for selling

    Matches Orders from Buy_Map and Sell_Map to fufill orders
    Fullfilled orders are returned as an array, in the form of:
    [Price, Asset, Seller_ID, Buyer_ID, Volume]
    """

    def __init__(self, asset_id):
        self.Buy_Map = PriceMap()
        self.Sell_Map = PriceMap()
        self.asset = asset_id


    def get_data(self):
        data = []
        data.append(self.Buy_Map)
        data.append(self.Sell_Map)

        return data

    def get_best_ask(self):
        return self.Sell_Map.get_min()

    def get_best_bid(self):
        return self.Buy_Map.get_max()

    def match_orders(self):
        fulfilled_orders = []

        best_bid_order = self.Buy_Map.extract_max()
        best_ask_order = self.Sell_Map.extract_min()

        best_bid_price = best_bid_order.get_price()
        best_ask_price = best_ask_order.get_price()

        while (best_bid_price >= best_ask_price):
            volume = min(best_bid_order.get_volume(), best_ask_order.get_volume())

            if (volume > 0):
                best_bid_order.decrease_volume(volume)
                best_ask_order.decrease_volume(volume)

                order_array = [best_bid_price, self.asset,
                               best_bid_order.get_owner(), best_ask_order.get_owner(),
                               volume]
                fulfilled_orders.append(order_array)

            if (best_bid_order.get_volume() != 0):
                self.Buy_Map.insert(best_bid_order)

            if (best_ask_order.get_volume() != 0):
                self.Sell_Map.insert(best_ask_order)

            best_bid_order = self.Buy_Map.extract_max()
            best_ask_order = self.Sell_Map.extract_min()

            best_bid_price = best_bid_order.get_price()
            best_ask_price = best_ask_order.get_price()

        return fulfilled_orders

    def add_order(self, order):
        if (order.get_type == 0):
            self.Buy_Map.insert(order)
        if (order.get_type == 1):
            self.Sell_Map.insert(order)
        else:
            raise ValueError("Invalid Order Type")




