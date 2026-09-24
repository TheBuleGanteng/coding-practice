'''
Function named "def second_most_common(text: str) -> str | None:"
Case-insensitive: "The" and "the" are the same word. Return it lowercased.
Split on whitespace. Punctuation stays attached, so "cat." and "cat" are different words.
Rank by count descending. Break ties alphabetically.
Return the word in 2nd place, or None if there are fewer than 2 distinct words.
'''

def second_most_common(text: str) -> str | None:
    ranked = {}
    formatted = text.lower().split() # Split on spaces and lowercase (default for split() is on spaces)
    for word in formatted: # iterate aross each word in the text
        ranked[word] = ranked.get(word, 0) + 1 # Look in the ranked dict for the current word. if it's not there, insert with value 0. Then in either case, increment value by 1
    
    sorted_data = sorted(ranked.items(), key=lambda kv: (-kv[1], kv[0])) # Sort items by count, with word as tiebreaker
    
    if len(sorted_data) > 1:
        return sorted_data[1][0] 
    else: 
        return None    
    print(sorted_data)
    print(sorted_data[1][0])


    
assert second_most_common("the cat and the hat and the bat") == "and"
assert second_most_common("Apple apple banana") == "banana"
assert second_most_common("hello hello hello") is None
assert second_most_common("") is None
assert second_most_common("b a") == "b"
assert second_most_common("x y y z z") == "z"
print("all tests passed")