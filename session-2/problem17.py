'''
Session 2, Problem 17b: Price history (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, and run one example call through it.

Write a class that records each product's price over time, keeping every change.

Class name: PriceHistory

Creating a PriceHistory() takes no arguments, and a new history starts empty.

For any one product, the timestamps in successive set_price calls always strictly increase.

Methods:

set_price(product, price, timestamp): product is a string, price is a positive int, timestamp is a non-negative int. Records that the product's price became price at time timestamp, keeping all earlier prices. Returns nothing.
price_at(product, timestamp): product is a string, timestamp is a non-negative int. Returns the product's price at that time: the price recorded at the largest timestamp less than or equal to timestamp, as an int. Returns None if the product doesn't exist or has no price recorded at or before timestamp.
current_price(product): product is a string. Returns the most recently recorded price for the product, as an int, or None if the product doesn't exist.
'''
class PriceHistory:
    
    def __init__(self):
        self.records: dict[str, dict] = {} # Dict w/ key=product and inner dict w/ k=timestamp and v=price
        
    '''1. set_price(product, price, timestamp): product is a string, price is a positive int, timestamp is a non-negative int. 
    Records that the product's price became price at time timestamp, keeping all earlier prices. 
    Returns nothing.'''     
    def set_price(self, product: str, price: int, timestamp: int):
        # If product is new, create it and set the inner dict
        if self.records.get(product, None) is None:
            self.records[product] = {timestamp:price}
        # If product already in records, simply set inner dict
        else:
            self.records[product][timestamp] = price
    
    '''2. price_at(product, timestamp): product is a string, timestamp is a non-negative int. 
    Returns the product's price at that time: the price recorded at the largest timestamp less than or equal to timestamp, as an int. 
    Returns None if the product doesn't exist or has no price recorded at or before timestamp.''' 
    def price_at(self, product: str, timestamp: int):
        product_data = self.records.get(product, None) 
        print(f'product_data: {product_data}, timestamp: {timestamp}')
        # If the product is in records, check if there is a price at timestamp
        if product_data is not None:
            result = None
            for prod_timestamp, prod_price in product_data.items():
                if prod_timestamp > timestamp:
                    break                  # everything after this is later too
                result = prod_price        # latest qualifying price so far
            return result
        # Return None if product isn't in records
        return None
    
    '''3. current_price(product): product is a string. 
    Returns the most recently recorded price for the product, as an int, or None if the product doesn't exist.'''
    def current_price(self, product: str):
        product_data = self.records.get(product, None) 
        if product_data is not None:
            solution = sorted(product_data.items(), key=lambda kv:(-kv[1], kv[0]))[0]
            print(f'{solution}')
        return None

# Example tests:


history = PriceHistory()
history.set_price("apple", 100, 10)
history.set_price("apple", 120, 20)
assert history.price_at("apple", 15) == 100
assert history.price_at("apple", 20) == 120

history = PriceHistory()
history.set_price("apple", 100, 10)
assert history.price_at("apple", 5) is None