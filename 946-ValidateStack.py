# 946. Validate Stack Sequences

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        curr = popped[0]
        while popped != []:
            if stack == [] or curr != stack[-1]:
                if pushed == []: return False
                stack.append(pushed.pop(0))
            else: # first el of popped is same as last el of stack
                stack.pop()
                popped.pop(0)
                try: curr = popped[0]
                except: return True
        return True

# works, medium fast, fairly low memory (in comparison to other answers)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        curr = None
        while popped != []:
            curr = popped[0]
            if stack == [] or curr != stack[-1]:
                if pushed == []: return False
                stack.append(pushed.pop(0))
            else: # first el of popped is same as last el of stack
                stack.pop()
                popped.pop(0)
        return True
