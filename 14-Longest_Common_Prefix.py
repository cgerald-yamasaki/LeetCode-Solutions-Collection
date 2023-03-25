# 14. Longest Common Prefix

# Write a function to find the longest common prefix string
# amongst an array of strings.
# If there is no common prefix, return an empty string "".

# works, got 98.59th percentile for runtime once, 6th-38.67th percentile for memory
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)
        for s in strs:
            if pref == "": return pref
            s_len = len(s)
            if s_len < pref_len:
                pref = pref[:s_len]
                pref_len = s_len
            for l_in in range(s_len):
                if l_in >= pref_len:
                    break
                if s[l_in] != pref[l_in]:
                    pref = pref[:l_in]
                    pref_len = l_in
                    break
        return pref

# works, 13.87th-67.55th percentile for runtime, 6th-79.5th for memory
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         pref = strs[0]
#         for s in strs:
#             if pref == "": return pref
#             if len(s) < len(pref): pref = pref[:len(s)]
#             for l_in in range(len(s)):
#                 if l_in >= len(pref):
#                     break
#                 if s[l_in] != pref[l_in]:
#                     pref = pref[:l_in]
#                     break
#         return pref
