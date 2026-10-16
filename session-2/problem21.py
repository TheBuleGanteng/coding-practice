'''
Session 2, Problem 21: Account ledger (progressive). Level 1

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Before coding: write __init__ with an example comment, run one example call through it, and check which row of your structures table this is.

Write a class that records money moving in and out of accounts over time.

Class name: Ledger

Creating a Ledger() takes no arguments, and a new ledger starts empty.

For any one account, the timestamps in successive record calls always strictly increase.

Methods:

record(account, amount, timestamp): account is a string, amount is an int (positive for money in, negative for money out), timestamp is a non-negative int. Records the entry. Returns the account’s balance after this entry, as an int: the sum of all its amounts so far.
balance_at(account, timestamp): account is a string, timestamp is a non-negative int. Returns the account’s balance at that time: the sum of all amounts recorded at or before timestamp, as an int. Returns 0 if the account doesn’t exist or has no entries at or before timestamp.
entry_count(account): account is a string. Returns the number of entries recorded for the account, as an int, or 0 if the account doesn’t exist.

-------------------
Session 2, Problem 21: Account ledger. Level 2

Time limit: 25 minutes, including writing your own tests. Aim for working code by about minute 20. Hard stop at 37 minutes. Start with your one-line variable list and one example call through your structure.

Add two methods to your Ledger class. Everything from Level 1 must keep working.

New methods:

net_change(account, start, end): account is a string; start and end are non-negative ints with start ≤ end. Returns the sum of the account’s amounts recorded at timestamps from start to end, inclusive, as an int. Returns 0 if the account doesn’t exist or has no entries in that range.
richest(timestamp, n): timestamp and n are non-negative ints. Returns a list of the n accounts with the highest balance at time timestamp, each as a string in the format "account(balance)". Only accounts with at least one entry at or before timestamp are included. The list is sorted by balance, largest first; accounts with equal balances are sorted alphabetically. If fewer than n accounts qualify, returns all of them.

'''

class Ledger:
    
    def __init__(self):
        self.records: dict[str, dict[int, int]] = {} # k = account (str) k=ts (int) v= amount (int)

    '''1. record(account, amount, timestamp): account is a string, amount is an int (positive for money in, negative for money out), timestamp is a non-negative int. 
    Records the entry. 
    Returns the account’s balance after this entry, as an int: the sum of all its amounts so far.'''
    def record(self, account: str, amount: int, timestamp: int):
        account_data = self.records.get(account, None)
        # If no account data, initialize with this txn
        if account_data is None:
            self.records[account] = {timestamp: amount}
            return amount
        # Initialize total to 0
        total = 0
        # Record txn
        self.records[account][timestamp] = amount
        # Loop over txns, summing them
        for timestamp, amount in account_data.items():
            total += amount
        #print(f'total: {total}')
        # Return the balance
        return total
               


    '''2. balance_at(account, timestamp): account is a string, timestamp is a non-negative int. 
    Returns the account’s balance at that time: the sum of all amounts recorded at or before timestamp, as an int. 
    Returns 0 if the account doesn’t exist or has no entries at or before timestamp.'''
    def balance_at(self, account: str, timestamp: int):
        account_data = self.records.get(account, None)
        # return 0 if no account
        if account_data is None:
            return 0
        # Initialize total to 0
        total = 0
        # Loop over txns, summing them
        for txn_timestamp, txn_amount in account_data.items():
            if txn_timestamp > timestamp:
                break
            total += txn_amount
        # print(f'total: {total}')
        # Return the balance
        return total
        

    '''3. entry_count(account): account is a string. 
    Returns the number of entries recorded for the account, as an int, or 0 if the account doesn’t exist.'''
    def entry_count(self, account: str):
        account_data = self.records.get(account, None)
        print(f'account_data: {account_data}')
        if account_data is None:
            return 0
        solution = len(account_data)        
        print(f'solution: {solution}')
        return solution
    
    '''4. net_change(account, start, end): account is a string; start and end are non-negative ints with start ≤ end. 
    Returns the sum of the account’s amounts recorded at timestamps from start to end, inclusive, as an int. 
    Returns 0 if the account doesn’t exist or has no entries in that range.'''
    def net_change(self, account: str, start: int, end: int):
        account_data = self.records.get(account, None)
        # return 0 if no account
        if account_data is None:
            return 0
        # Total 
        total = sum(txn for timestamp, txn in account_data.items() if (timestamp >= start and timestamp <= end))
        return total
    
    '''5. richest(timestamp, n): timestamp and n are non-negative ints. 
    Returns a list of the n accounts with the highest balance at time timestamp, each as a string in the format "account(balance)". 
    Only accounts with at least one entry at or before timestamp are included. 
    The list is sorted by balance, largest first; accounts with equal balances are sorted alphabetically. 
    If fewer than n accounts qualify, returns all of them.'''
    def richest(self, timestamp: int, n: int):
        # initialize dict w/ k=account, v = blance
        accounts_dict = {}
        for account, txns in self.records.items():
            # Get the timestamp corresponding to this count's first txn and compare it to timestamp to ensure there is at least 1 qualifying txn
            if next(iter(txns)) <= timestamp:
                accounts_dict[account] = self.balance_at(account=account, timestamp=timestamp)
        sorted_acts = sorted(accounts_dict.items(), key=lambda kv:(-kv[1], kv[0]))
        formatted_acts = [f'{account}({balance})' for account, balance in sorted_acts[:n]]        
        print(f'formatted_acts: {formatted_acts}')
        return formatted_acts
    
# Complexity:
# a = total accounts
# x = txns for a given account
# t = total txns 
# 1. record --> loop over the txns for a given account --> O(x)
# 2. balance_at --> loop over the txns for a given account --> O(x)
# 3. entry_count: O(1)

# Worst case complexity: O(x)
# Memory: O(a + t)

# Example tests:

ledger = Ledger()
assert ledger.record("ann", 100, 10) == 100
assert ledger.record("ann", -30, 20) == 70
assert ledger.balance_at("ann", 15) == 100
assert ledger.balance_at("bob", 15) == 0 # account doesn't exist
assert ledger.record("ann", -70, 25) == 0 
assert ledger.balance_at("ann", 25) == 0 # Balance of 0
assert ledger.entry_count("ann") == 3 # Happy path
assert ledger.entry_count("bob") == 0 # account doesn't exist


ledger = Ledger()
assert ledger.balance_at("ann", 15) == 0


ledger = Ledger()
ledger.record("ann", 100, 10)
ledger.record("ann", -30, 20)
ledger.record("ann", 50, 30)
assert ledger.net_change("ann", 15, 30) == 20


ledger = Ledger()
ledger.record("ann", 100, 10)
ledger.record("bob", 200, 10)
ledger.record("cat", 500, 50)
assert ledger.richest(20, 3) == ["bob(200)", "ann(100)"]

print('all tests pass')