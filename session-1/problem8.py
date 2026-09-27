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


# Iterate across the chars in text. 
# If a bracket is detected, determine (a) the type and (b) opening or closing
# If opening: create a dict with key = type and value = position in text
# If closing: check dict to see if (a) there is a corresponding opening bracket (return Fales if no), (b) the position of the corresponding backet is the smallest value. if yes, remove the corresponding bracket from the dict and move on

def is_balanced(text: str):
    print(f'text: {text}')  
    
    brackets = ['(', ')', '[',']', '{', '}']
    brakets_opening = ['(', '[', '{']
    brakets_closing = [')', ']', '}']
    
    latest = [] # List to hold opening chars
    
    for char in text:
        #print(f'examining i: {i}, char: {char}')
        
        
        if char not in brackets:
            continue
        
        if char in brakets_opening:
            latest.append(char)
            print(f'latest updated to: {latest}')
            continue
        
        if char in brakets_closing and len(latest) == 0:
            return False
        
        # For all three closers: If the current char is a closer, check if latest is the correct opener. 
        # If yes, then remove that most recent opener
        # If no, return False
        elif char == ')':
            if latest[-1] != '(':
                print(f'char: {char} doesnt correspond to latest: {latest}')
                return False
            else:
                print(f'removing latest[-1]: {latest[-1]}')
                latest.pop()
                
        elif char == ']':
            if latest[-1] != '[':
                print(f'char: {char} doesnt correspond to latest: {latest}')
                return False
            else:
                print(f'removing latest[-1]: {latest[-1]}')
                latest.pop()
        
        elif char == '}':
            if latest[-1] != '{':        
                print(f'char: {char} doesnt correspond to latest: {latest}')
                return False
            else:
                print(f'removing latest[-1]: {latest[-1]}')
                latest.pop()

    # Ensures there are no openers left without closers
    if len(latest) != 0:
        return False
    
    return True

# Complexity:
# 1. Loop through chars: O(n)
# 2. No scaling within the loop, each loop does same amount of work


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