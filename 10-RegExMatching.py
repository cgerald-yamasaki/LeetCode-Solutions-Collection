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
