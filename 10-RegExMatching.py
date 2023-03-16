# 10. Regular Expression Matching
# Given an input string s and a pattern p, implement regular expression
# matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# works, slowish, middle of the road for memory
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        new_p = p[0]
        for p_in in range(1, len(p)):   # get rid of redundancies
            if p[p_in] == '*':
                if len(new_p) >= 3:
                    if new_p[-2] == '*' and (new_p[-3] == new_p[-1] or new_p[-3] == '.'):
                        new_p = new_p[0: -1]    # cut off most recent character
                        continue
                    if new_p[-2] == '*' and new_p[-1] == '.':
                        new_p = new_p[0: -3] + ".*"
                        continue
                elif new_p[-1] == '*': 
                    continue
            new_p = new_p + p[p_in]
        def canBeNothing(p: str) -> bool:
            while p != "":
                if len(p) > 1 and p[1] == '*':
                    p = p[2:]
                elif p[0] == '*':
                    p = p[1:]
                else: return False
            return True
        curr_l = [0]
        for curr_p_in in range(len(new_p)):
            cl_len = len(curr_l)
            to_remove = []
            for cl_in in range(cl_len):
                if curr_p_in + 1 < len(new_p) and new_p[curr_p_in + 1] == '*':
                    curr_l.append(curr_l[cl_in])
                if curr_l[cl_in] >= len(s):
                    if canBeNothing(new_p[curr_p_in:]): return True
                    to_remove.append(curr_l[cl_in])
                    continue
                if new_p[curr_p_in] == '.' or new_p[curr_p_in] == s[curr_l[cl_in]]:
                    curr_l[cl_in] = curr_l[cl_in] + 1
                    continue
                if new_p[curr_p_in] == '*':
                    if new_p[curr_p_in - 1] == '.':
                        s_in = curr_l[cl_in]
                        while s_in < len(s):
                            curr_l.append(s_in + 1)
                            s_in += 1
                    elif new_p[curr_p_in - 1] == s[curr_l[cl_in]]:
                        s_in = curr_l[cl_in]
                        while s_in < len(s) and s[s_in] == s[curr_l[cl_in]]:
                            curr_l.append(s_in + 1)
                            s_in += 1
                    continue
                to_remove.append(curr_l[cl_in])
            for tr in to_remove: curr_l.remove(tr)
        if len(s) in curr_l: return True
        return False


# Previous failed ideas:

# going through s rather than p
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         curr_p = [0]
#         for l in s: # check each letter in s
#             curr_p_len = len(curr_p)
#             to_remove = []
#             for cp_in in range(curr_p_len):    # check each branching path of p possibilities
#                 if curr_p[cp_in] >= len(p):  # if this path already finished p with letters of s left, remove path
#                     curr_p.remove(curr_p[cp_in])
#                     continue
#                 if len(p) > curr_p[cp_in] + 1 and p[curr_p[cp_in] + 1] == '*': # case where * means zero
#                     cp = curr_p[cp_in] + 1
#                     while cp < len(p) and p[cp] == '*':
#                         cp += 1
#                     # now cp is the first index of p that is not a '*'
#                     if cp < len(p) and (l == p[cp] or p[cp] == '.'):
#                         curr_p.append(cp + 1)
#                         print(cp + 1)
#                 print(l, p[curr_p[cp_in]])
#                 if l == p[curr_p[cp_in]] or p[curr_p[cp_in]] == '.':
#                     curr_p[cp_in] += 1
#                     continue
#                 if p[curr_p[cp_in]] == '*':
#                     print(p[curr_p[cp_in] - 1])
#                     if l == p[curr_p[cp_in] - 1] or p[curr_p[cp_in] - 1] == '.':
#                         curr_p.append(curr_p[cp_in] + 1)
#                         continue
#                 to_remove.append(curr_p[cp_in])
#                 # curr_p.remove(curr_p[cp_in])    # if l didn't match path, remove possible pattern path
#             for tr in to_remove:
#                 curr_p.remove(tr)
#         print(len(p), curr_p)
#         if len(p) in curr_p: return True    # if reached end of s and one of the paths also completed p
#         else: return False

# didn't realize * could be zero
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         curr_p = [0]
#         for l in s: # check each letter in s
#             curr_p_len = len(curr_p)
#             for cp_in in range(curr_p_len):    # check each branching path of p possibilities
#                 if curr_p[cp_in] >= len(p):  # if this path already finished p with letters of s left, remove path
#                     curr_p.remove(curr_p[cp_in])
#                     continue
#                 print(l, p[curr_p[cp_in]])
#                 if l == p[curr_p[cp_in]] or p[curr_p[cp_in]] == '.':
#                     curr_p[cp_in] += 1
#                     continue
#                 if p[curr_p[cp_in]] == '*':
#                     print(p[curr_p[cp_in] - 1])
#                     if l == p[curr_p[cp_in] - 1] or p[curr_p[cp_in] - 1] == '.':
#                         curr_p.append(curr_p[cp_in] + 1)
#                         continue
#                     # cover case where "**"?
#                 curr_p.remove(curr_p[cp_in])    # if l didn't match path, remove possible pattern path
#         print(len(p), curr_p)
#         if len(p) in curr_p: return True    # if reached end of s and one of the paths also completed p
#         else: return False