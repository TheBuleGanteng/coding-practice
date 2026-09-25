'''
Drill C: Filter and summarize transactions

python
def summarize(transactions: list[str], min_total: float) -> list[tuple[str, float]]:
    ...
Each transaction is a string in the form "date|category|amount", for example "2026-09-01|food|12.50".
1. Skip malformed lines, meaning any line that doesn't have exactly 3 fields.
2. Add up the amounts per category.
3. Keep only categories whose total is at least min_total. The comparison is inclusive.
4. Return a list of (category, total) tuples, highest total first, with ties broken alphabetically.

data = [
    "2026-09-01|food|12.50",
    "2026-09-01|transport|3.25",
    "2026-09-02|food|7.50",
    "2026-09-02|rent|500.00",
    "2026-09-03|transport|4.75",
    "bad line",
    "2026-09-04|books|20.00",
]

assert summarize(data, 10) == [("rent", 500.0), ("books", 20.0), ("food", 20.0)]
assert summarize(data, 20) == [("rent", 500.0), ("books", 20.0), ("food", 20.0)]
assert summarize(data, 20.01) == [("rent", 500.0)]
assert summarize(data, 1000) == []
assert summarize([], 0) == []
assert summarize(data, 0) == [("rent", 500.0), ("books", 20.0), ("food", 20.0), ("transport", 8.0)]
print("all tests passed")

When you're done, paste the code, the terminal output, and the complexity with the reason for each step's cost. 
Say what n and m stand for.
'''

def summarize(transactions: list[str], min_total: float) -> list[tuple[str, float]]:
    print('running summarize()...')
    totals = {} # Dict to hold spending by category
    
    for item in transactions:
        parsed = item.split("|") # Parse the strings
        
        # Req 1: Skip malformed lines
        if len(parsed) != 3:
            continue
        
        date, category, price = parsed[0], parsed[1], float(parsed[2]) # Assign each component a variable
        
        # Req 2: Add the prices per category
        totals[category] = totals.get(category, 0) + price
        
    # Req 3: Keep only categories whose total is at least min_total. The comparison is inclusive.
    print(f'before filtering, totals is: {totals}')
    totals_filtered = {} # New dict for the filtered totals (e.g. exclude categories below min spend)
    for category, amount in totals.items():
        print(f'category, amount is:{category, amount}')
        if amount >= min_total:
            totals_filtered[category] = amount # Add items from old dict to new dict if at or above min spend
            
    # Req 4: Return a list of (category, total) tuples, highest total first, with ties broken alphabetically.
    totals_filtered = sorted(totals_filtered.items(), key=lambda kv:(-kv[1], kv[0]))
    return totals_filtered
    
    # Req 5: Complexity with the reason for each step's cost
    # Complexity = O(n + m + a log a (
        # n = runs once per line in orig. list to generate per-category totals, 
        # m = runs once per line in the list of unique category totals to exclude totals below minimum threshold
        # a log a = filters list of unique categories that meet min. spending
        # )

# Testing cases
data = [
    "2026-09-01|food|12.50",
    "2026-09-01|transport|3.25",
    "2026-09-02|food|7.50",
    "2026-09-02|rent|500.00",
    "2026-09-03|transport|4.75",
    "bad line",
    "2026-09-04|books|20.00",
]

assert summarize(data, 10) == [("rent", 500.0), ("books", 20.0), ("food", 20.0)]
assert summarize(data, 20) == [("rent", 500.0), ("books", 20.0), ("food", 20.0)]
assert summarize(data, 20.01) == [("rent", 500.0)]
assert summarize(data, 1000) == []
assert summarize([], 0) == []
assert summarize(data, 0) == [("rent", 500.0), ("books", 20.0), ("food", 20.0), ("transport", 8.0)]
print("all tests passed")
    
    