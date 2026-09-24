'''
Function named "def second_most_common(text: str) -> str | None:"
Case-insensitive: "The" and "the" are the same word. Return it lowercased.
Split on whitespace. Punctuation stays attached, so "cat." and "cat" are different words.
Rank by count descending. Break ties alphabetically.
Return the word in 2nd place, or None if there are fewer than 2 distinct words.
'''

def second_most_common(text: str) -> str | None:
    words = {}
    
    formatted = text.lower().split() # Lowercase and split text on spaces
    
    for word in formatted:
        words[word] = words.get(word, 0) + 1 # Check to see if word is already in the words dict. If not, add it. In either case, increment the count by 1
        
    ranked = sorted(words.items(), key=lambda kv:(-kv[1], kv[0])) # Sort by count with word as tiebreaker
    
    if len(ranked) < 2:
        return None
    else:
        return ranked[1][0]
        
    
assert second_most_common("the cat and the hat and the bat") == "and"
assert second_most_common("Apple apple banana") == "banana"
assert second_most_common("hello hello hello") is None
assert second_most_common("") is None
assert second_most_common("b a") == "b"
assert second_most_common("x y y z z") == "z"
print("all tests passed")


# Question: What is time complexity in terms of n (number of words)?
# Answer: The complexity is n + m log m wherein n = number of words and m = number of unique words. Best case scenario, 1 unique word, so time is n. Worst case scenario, all are unique words, so time is n + n log n.