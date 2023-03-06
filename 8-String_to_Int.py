# String to Integer (atoi)

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.

# if s has letters before numbers, return 0?
# ... according to testcases, yes, return 0 if s has letters before numbers

# wrote in 2147483648 instead of 2^31, 94.8th percentile for runtime,
# 98.24th for memory (...sometimes. I do think it's at least some amount better than prev sol)
class Solution:
    def myAtoi(self, s: str) -> int:
        ret_num = 0
        sign = 1    # 1 for positive, -1 for negative
        num_started = False
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for c in s:
            if c in digits:
                ret_num = (ret_num * 10) + int(c)
                if ret_num > 2147483648 and sign == -1:
                    return -2147483648
                elif ret_num > 2147483647 and sign == 1:
                    return 2147483647
                num_started = True
                continue
            elif num_started:
                return ret_num * sign
            elif c == ' ': continue
            elif c == '-':
                sign = -1
                num_started = True
                continue
            elif c == '+':
                num_started = True
                continue
            else: return ret_num * sign
        return ret_num * sign

# works, 27.79th percentile for runtime, 13.8th for memory
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         ret_num = 0
#         sign = 1    # 1 for positive, -1 for negative
#         num_started = False
#         digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         for c in s:
#             if c in digits:
#                 ret_num = (ret_num * 10) + int(c)
#                 if ret_num > 2 ** 31 and sign == -1:
#                     return (2 ** 31) * -1
#                 elif ret_num > (2 ** 31) - 1 and sign == 1:
#                     return (2 ** 31) - 1
#                 num_started = True
#                 continue
#             elif num_started:
#                 return ret_num * sign
#             elif c == ' ': continue
#             elif c == '-':
#                 sign = -1
#                 num_started = True
#                 continue
#             elif c == '+':
#                 num_started = True
#                 continue
#             else: return ret_num * sign
#         return ret_num * sign
