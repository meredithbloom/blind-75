# 20. Valid Parentheses
# given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

'''
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

# constraints
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def isValid(s):
    stack = []
    print(s)
    for elem in s:
        if elem == '(' or elem == '[' or elem == '{':
            stack.append(elem)
        elif len(stack) == 0 and (elem == ')' or elem == ']' or elem =='}'):
            return False
        elif elem == ')' and stack[len(stack)-1] == '(':
            stack.pop()
        elif elem == ']' and stack[len(stack)-1] == '[':
            stack.pop()
        elif elem == '}' and stack[len(stack)-1] == '{':
            stack.pop()
        else:
            return False 
    if len(stack) > 0:
        return False   
    else:
        return True
    
    
    
isValid('()')
isValid("()[]{}")
isValid('(]')
isValid('{[]}')
