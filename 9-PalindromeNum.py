# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome,
# and false otherwise.

# got idea for this solution from a posted solution in C++
# memory and runtime ratings kinda all over the place over three identical submissions
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0: return False
#         y = x
#         rev = 0
#         while y > 0:
#             rev = (rev * 10) + (y % 10)
#             y = y // 10
#         return x == rev

# slower, ~15th percentile for runtime, but sometimes 93.7th for memory
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0: return False
#         elif x < 10: return True
#         s = str(x)
#         slen = len(s)
#         while slen > 1:
#             if s[0] != s[slen - 1]:
#                 return False
#             else:
#                 s = s[1:slen - 1]
#                 slen -= 2
#         return True

# works, ~50.22nd percentile for runtime, 47.9th for memory
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        elif x < 10: return True    # could take this line out
        s = str(x)
        while len(s) > 1:
            if s[0] != s[len(s) - 1]:
                return False
            else:
                s = s[1:len(s) - 1]
        return True