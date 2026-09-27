'''
Problem 8: Validate template brackets

A config system uses templates that can contain three kinds of brackets: (), [] and {}. 
Before rendering a template, it has to check that the brackets are valid.

Function name: is_balanced

Argument:

text: a string. It can contain any characters, not just brackets.

Requirements:

Return True if the brackets are valid, and False otherwise.
Valid means:
1. Every opening bracket has a matching closing bracket of the same type.
2. Brackets close in the right order. The most recently opened bracket must be the first one closed.
3. No closing bracket appears without an earlier open bracket for it to close.
4. Ignore every character that isn't a bracket.
An empty string, or a string with no brackets, is valid.
'''

def is_balanced(text: str):
    print(f'text: {text}')  
    
    openers = [] # Holds opening brakets encountered
    
    brackets = {')':'(', ']':'[', '}':'{'} # Dict to hold opening and closing bracket pairs
    print(f'brackets: {brackets}')
    
    for char in text:
        print(f'analyzing char: {char}')
        
        # ignore non-bracket chars
        if char not in brackets and char not in brackets.values():
            continue
        
        # Return false if there is a closer without any openers
        if char in brackets and len(openers) == 0:
            print(f'closing bracket w len(openers) == 0, returning False')
            return False
        
        # if it's an opening bracket, append to openers
        if char in brackets.values():
            openers.append(char)
            print(f'appended: {char} to openers, updated openers: {openers}')
    
        # if it's a closing bracket, check the last item in openers to see if it's the matching value in the dict
        else:
            # If it's a closing bracket and the most recent opener is the match, then remove that opener from the dict
            print(f'comparing brackets.get(char): {brackets.get(char)} and openers[-1]: {openers[-1]}')
            if brackets.get(char) == openers[-1]:
                openers.pop()
                print(f'removed: {char} from openers. Updated openers: {openers}')
            else:
                return False
    
    # Guard against any random openers without closers
    return len(openers) == 0

# Complexity:
# 1. Loop through chars: O(n)
# 2. No scaling within the loop, each loop does same amount of work
# Result: O(n) with O(n) memory


# Test cases
assert is_balanced("") == True
assert is_balanced("no brackets here") == True
assert is_balanced("config(a[1]{x})") == True
assert is_balanced("{[()()]}") == True
assert is_balanced("(]") == False
assert is_balanced("((") == False
assert is_balanced("))") == False
assert is_balanced("([)]") == False
assert is_balanced("a)b(c") == False
print("all tests passed")