# 20. Valid Parentheses

# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the input string
# is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# works, 67.76th percentile for runtime, 16.94th for memory
class Solution:
    def isValid(self, s: str) -> bool:
        close_stack = []
        for p in s:
            if p == '(':
                close_stack.append(')')
                continue
            elif p == '{':
                close_stack.append('}')
                continue
            elif p == '[':
                close_stack.append(']')
                continue
            if close_stack == []: return False
            close = close_stack.pop()
            print(p, close)
            if p != close: return False
        if close_stack == []: return True
        print(close_stack)
        return False
