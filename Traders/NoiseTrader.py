import numpy as np
import Trader

class NoiseTrader(Trader):
    """
    NoiseTrader Class: Nickname SillySally
    Inherets functions from Trader
    """

    def __init__(self, starting_cash, num_assets, sd):
        self.asset_count = num_assets
        self.cash = starting_cash

        self.portfolio = np.zeros(num_assets)  # Initialize with zeros
        self.value = starting_cash
        self.sd = sd
    
    def mark_to_market(self):
        self.value = self.cash + np.dot(self.portfolio[1:], self.spot_prices)  # Vectorized calculation

    def recieve_spot_prices(self, market_prices):
        self.spot_prices = np.array(market_prices)  # Convert to NumPy array

    def pricing_algorithm(self):
        asset_index = np.random.uniform(1, self.asset_count)
        current_price = self.spot_prices[asset_index]

        expected_value = current_price * np.exp(np.random.normal(loc=0, scale=self.sd))

        return expected_value
    
    def place_order(self):
        return
    
