from abc import ABC, abstractmethod

class Trader(ABC):
    """
    Trader Abstract Class

    All Traders Have the same base functions:

    recieve_spot(): get the current spot prices for each asset

    recieve_time_series(): get time series for each asset

    pricing_algorithm() : compute EV for each asset

    place_order(): Depending on EV calc, place order
    """

    @abstractmethod
    def mark_to_market():
        pass

    @abstractmethod
    def recieve_spot_prices():
        pass

    @abstractmethod
    def recieve_time_series():
        pass

    @abstractmethod
    def pricing_algorithm():
        pass

    @abstractmethod
    def place_order():
        pass
