'''
Session 2, Problem 3: Bank

Time limit: 25 minutes, including writing your own tests. 
Aim for working code by about minute 20. 
Hard stop at 37 minutes; if you reach it, switch to studying a solution and retype it cold tomorrow.

Write a class that tracks bank account balances.

Class name: Bank

Creating a Bank() takes no arguments, and a new bank starts with no accounts.

Methods:

1. open_account(account_id): account_id is a string. Creates a new account with a balance of 0. 
Returns True if the account was created, or False if an account with that id already exists (the existing account is left unchanged).
2. deposit(account_id, amount): account_id is a string, amount is a positive int. 
Adds amount to the account's balance and returns the new balance as an int. 
Returns None if the account doesn't exist.
3. withdraw(account_id, amount): account_id is a string, amount is a positive int. 
Subtracts amount from the account's balance and returns the new balance as an int. 
Returns None if the account doesn't exist, or if the balance is less than amount; in that case the balance is unchanged.
4. balance(account_id): account_id is a string. 
Returns the account's current balance as an int, or None if the account doesn't exist.
'''
'''
Variables:
account_id (str)
amount (int)
Classes
1. Bank -- no arguments
'''

class Bank:
    
    def __init__(self):
        self.records: dict[str, int] = {}
        
    def open_account(self, account_id: str):
        account_balance = self.records.get(account_id, None) # I return None istead of 0 to distinguish between an already-open account with 0 and an account that doesn't yet exist
        if account_balance is None: # Account doesn't exist. Create a new one w/ balance = 0, per spec
            self.records[account_id] = 0 # Update records
            return True # Return True, per spec
        else: # Don't do anything, other than return False, per spec
            return False
    
    def deposit(self, account_id: str, amount:int):
        account_balance = self.records.get(account_id, None)
        if account_balance is None: # If account doesn't exist, return None per spec
            return None
        self.records[account_id] += amount # Increment the current total by amount
        return self.records[account_id] # Return new total, per spec

    def withdraw(self, account_id: str, amount: int):
        account_balance = self.records.get(account_id, None)
        if account_balance is None or account_balance < amount: # Per spec
            return None
        self.records[account_id] -= amount # Update and balance and return new balance, per spec
        return self.records[account_id]
    
    def balance(self, account_id: str):
        return self.records.get(account_id, None)

# Complexity: All methods are lookups/updates, O(1)
# Memory: O(a) w/ a = num of accounts

#Example tests:
bank = Bank()
# open_account tests
assert bank.open_account("a1") is True
assert bank.open_account("a1") is False # already open account returns False
# deposit tests
assert bank.deposit("a1", 50) == 50
assert bank.deposit("a1", 50) == 100
assert bank.deposit("a2", 50) is None
# withdraw tests
assert bank.withdraw("a1", 1) == 99
assert bank.withdraw("a1", 1000) is None
assert bank.withdraw("a2", 1) is None
# balance tests
assert bank.balance("a1") == 99
assert bank.balance("a2") is None

# perminance tests
bank2 = Bank()
assert bank.balance("a1") == 99
assert bank2.balance("a1") is None
print('all tests pass')