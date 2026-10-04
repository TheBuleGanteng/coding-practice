'''
Session 2, Problem 9: Banking system (progressive). Level 1

This problem has 3 levels. Each adds to the same class, and earlier levels must keep working.

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Write a class that manages bank accounts.

Class name: BankSystem

Creating a BankSystem() takes no arguments, and a new system starts with no accounts.

Methods:

1. create_account(account_id): account_id is a string. Creates an account with a balance of 0. Returns True if the account was created, or False if an account with that id already exists (the existing account is left unchanged).
2. deposit(account_id, amount): account_id is a string, amount is a positive int. Adds amount to the account's balance and returns the new balance as an int. Returns None if the account doesn't exist.
3. transfer(from_id, to_id, amount): from_id and to_id are strings, amount is a positive int. Moves amount from the first account to the second and returns the first account's new balance as an int. Returns None, with both balances unchanged, if either account doesn't exist, if from_id and to_id are the same, or if the first account's balance is less than amount.

----------------------------------------------------------------------------------------------------------

Session 2, Problem 9: Banking system. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with the design block.

Add two methods to your BankSystem class. Everything from Level 1 must keep working.

New methods:

4. balance(account_id): account_id is a string. Returns the account's current balance as an int, or None if the account doesn't exist.
5. top_spenders(n): n is a non-negative int. Returns a list of the n accounts that have sent the most money through successful transfers in total, each as a string in the format "account_id(total)". The list is sorted by total sent, largest first; accounts with equal totals are sorted alphabetically by id. Every account is included in the ranking, including accounts that have sent nothing (total 0). If there are fewer than n accounts, returns all of them.
----------------------------------------------------------------------------------------------------------
Session 2, Problem 9: Banking system. Level 3

Time limit: 35 minutes, including writing your own tests. Aim for working code by about minute 28. Hard stop at 52 minutes. Start with the design block, including: which existing methods will the new ones call, and what do those methods change?

Add the ability to freeze accounts for a period of time. Everything from Levels 1 and 2 must keep working, and the old transfer method ignores freezes.

Every new method takes a timestamp, a non-negative int. Timestamps in successive calls never decrease.

New methods:

freeze(account_id, timestamp, duration): account_id is a string, duration is a positive int. Freezes the account from timestamp up to, but not including, timestamp + duration. If the account is already frozen, the new freeze replaces the old one. Returns True if the account exists, or False if it doesn't.
is_frozen(account_id, timestamp): account_id is a string. Returns True if the account is frozen at time timestamp, or False otherwise, including when the account doesn't exist.
transfer_at(from_id, to_id, amount, timestamp): same as transfer, at time timestamp, except it also returns None, with both balances unchanged, if either account is frozen at timestamp.
----------------------------------------------------------------------------------------------------------

'''

class BankSystem:
    
    def __init__(self):
        self.records: dict[str, int] = {}
        self.transfers: dict[str, int] = {}
        self.freezes: dict[str, int] = {}
        
    '''1. create_account(account_id): account_id is a string. Creates an account with a balance of 0. 
    Returns True if the account was created, or False if an account with that id already exists (the existing account is left unchanged).'''
    def create_account(self, account_id: str):
        # Check to see if an account w/ this name already exists
        account_info = self.records.get(account_id, None)
        # If this account already exists, return False
        if account_info is not None:
            return False
        # Create account and return True
        self.records[account_id] = 0
        # Add account to transfers dict too
        self.transfers[account_id] = 0
        # Add account to the freezes dict too 
        self.freezes[account_id] = 0
        
        return True
        
    '''2. deposit(account_id, amount): account_id is a string, amount is a positive int. 
    Adds amount to the account's balance and returns the new balance as an int. 
    Returns None if the account doesn't exist.'''
    def deposit(self, account_id: str, amount: int):
        # Check if account exists
        account_info = self.records.get(account_id, None)
        # If account doesn't exist, return None
        if account_info is None:
            return None    
        # If account exists, add the amount and return the new balance
        self.records[account_id] += amount
        return self.records[account_id]
    
    '''3. transfer(from_id, to_id, amount): from_id and to_id are strings, amount is a positive int. 
    Moves amount from the first account to the second and returns the first account's new balance as an int. 
    Returns None, with both balances unchanged, if either account doesn't exist, if from_id and to_id are the same, 
    or if the first account's balance is less than amount.'''
    def transfer(self, from_id: str, to_id: str, amount: int):
        # Check if both accounts exist
        from_account_info = self.records.get(from_id, None)
        to_account_info = self.records.get(to_id, None)
        print(f'transfer...from_account_info: {from_account_info}, to_account_info: {to_account_info}')
        
        # If either account is missing, return None
        if from_account_info is None or to_account_info is None or from_id == to_id or from_account_info < amount:
            print(f'tansfer... returning None')    
            return None
        # If transfer is legit, move money and return first account's new balance
        from_account_info -= amount
        to_account_info += amount
        self.records[from_id] = from_account_info
        self.records[to_id] = to_account_info
        print(f'transfer...returning from_account_info: {from_account_info}')
        
        # Added for item 5, top_spenders
        # Update the transfers dict 
        self.transfers[from_id] += amount
        
        return from_account_info

    '''4. balance(account_id): account_id is a string. 
    Returns the account's current balance as an int, or None if the account doesn't exist.'''
    def balance(self, account_id: str):
        # Check if the account exists
        account_balance = self.records.get(account_id, None)
        # If not, return none
        if account_balance is None:
            return None
        # If yes, return the balance
        return account_balance

    '''5. top_spenders(n): n is a non-negative int. 
    Returns a list of the n accounts that have sent the most money through successful transfers in total, each as a string in the format "account_id(total)". 
    The list is sorted by total sent, largest first; accounts with equal totals are sorted alphabetically by id. Every account is included in the ranking, including accounts that have sent nothing (total 0). 
    If there are fewer than n accounts, returns all of them.'''
    def top_spenders(self, n: int):
        transfer_data = self.transfers.items()
        print(f'transfer_data: {transfer_data}')
        transfer_data_sorted = sorted(self.transfers.items(), key=lambda kv:(-kv[1], kv[0]))
        print(f'transfer_data_sorted: {transfer_data_sorted}')
        transfer_data_sorted_formatted = [(f'{sender}({amount})') for sender, amount in transfer_data_sorted][:n]
        return transfer_data_sorted_formatted
        

    '''6. freeze(account_id, timestamp, duration): account_id is a string, duration is a positive int. 
    Freezes the account from timestamp up to, but not including, timestamp + duration. 
    If the account is already frozen, the new freeze replaces the old one. 
    Returns True if the account exists, or False if it doesn't.'''
    def freeze(self, account_id: str, timestamp: int, duration: int):
        # Check if the account exists
        account_balance = self.records.get(account_id, None)
        # Return false if account doesn't exist
        if account_balance is None:
            return False
        # Set the freeze expiry and return True
        self.freezes[account_id] = timestamp + duration
        return True
    
    '''7. is_frozen(account_id, timestamp): account_id is a string. 
    Returns True if the account is frozen at time timestamp, or False otherwise, including when the account doesn't exist.'''
    def is_frozen(self, account_id: str, timestamp: int):
        # Get freeze date
        freeze_date = self.freezes.get(account_id, None)
        # If freeze date in in the future, account is frozen, return True
        if freeze_date is not None and timestamp < freeze_date:
            return True
        # Otherwise, return false
        return False

    '''8. transfer_at(from_id, to_id, amount, timestamp): same as transfer, at time timestamp, except it also 
    returns None, with both balances unchanged, if either account is frozen at timestamp.'''
    def transfer_at(self, from_id: str, to_id: str, amount: int, timestamp: int):
        # If either account is frozen, return None
        if self.is_frozen(from_id, timestamp) or self.is_frozen(to_id, timestamp):
            print(f'transfer_at...returning None')
            return None
        # If neither account is frozen, do the transfer
        return self.transfer(from_id=from_id, to_id=to_id, amount=amount)
            

# Complexity:
# 1. create_account --> O(1)
# 2. deposit --> O(1)
# 3. transfer --> O(1)
# 4. balance --> O(1)
# 5. top_spenders --> sorting of n accounts O(m log m) + list comprehension O(n) --> O(n log n)
# 6. freeze --> O(1)
# 7. is_frozen --> O(1)
# 8. transfer_at --> runs is_frozen twice O(1) + runs transfer O(1)
# Worst case: complxity: O(m log m) with O(m) m= number of accounts (three times bc 3 dicts)


# Example tests:
bank = BankSystem()
bank.create_account("a")
assert bank.create_account("a") is False

bank.create_account("b")
bank.deposit("a", 100)
assert bank.deposit("c", 100) is None
assert bank.transfer("a", "b", 30) == 70
assert bank.transfer("a", "c", 30) is None
assert bank.transfer("a", "b", 3000) is None
assert bank.transfer("c", "b", 30) is None
assert bank.transfer("a", "a", 30) is None

bank = BankSystem()
bank.create_account("a")
assert bank.transfer("a", "a", 10) is None

bank2 = BankSystem()
bank2.create_account("a")
bank2.create_account("b")
bank2.deposit("a", 100)
bank2.transfer("a", "b", 30)
assert bank2.balance("b") == 30
assert bank2.balance("c") is None
assert bank2.balance("a") == 70
bank2.transfer("a", "b", 70)
assert bank2.balance("a") == 0
assert bank2.balance("b") == 100


bank3 = BankSystem()
bank3.create_account("a")
bank3.create_account("b")
bank3.deposit("a", 100)
bank3.transfer("a", "b", 30)
assert bank3.top_spenders(2) == ["a(30)", "b(0)"]
assert bank3.top_spenders(100) == ["a(30)", "b(0)"]

bank4 = BankSystem()
bank4.create_account("a")
bank4.create_account("b")
assert bank4.top_spenders(100) == ["a(0)", "b(0)"]

bank5 = BankSystem()
bank5.create_account("a")
bank5.create_account("b")
bank5.transfer("a", "b", 30)
bank5.transfer("b", "a", 30)
assert bank5.top_spenders(100) == ["a(0)", "b(0)"]


bank = BankSystem()
bank.create_account("a")
assert bank.freeze("a", 10, 5) is True
assert bank.is_frozen("a", 14) is True
assert bank.is_frozen("a", 15) is False
assert bank.is_frozen("b", 15) is False

bank = BankSystem()
bank.create_account("a")
bank.create_account("b")
bank.deposit("a", 100)
bank.freeze("b", 10, 5)
assert bank.transfer_at("a", "b", 30, 12) is None
assert bank.transfer_at("a", "b", 30, 20) == 70
bank.freeze("1", 10, 5)
assert bank.transfer_at("a", "b", 30, 12) is None
assert bank.transfer_at("a", "c", 30, 12) is None
assert bank.transfer_at("a", "b", 3000, 12) is None


print('tests pass')