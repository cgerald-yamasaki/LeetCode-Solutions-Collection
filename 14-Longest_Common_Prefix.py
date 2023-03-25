# 14. Longest Common Prefix

# Write a function to find the longest common prefix string
# amongst an array of strings.
# If there is no common prefix, return an empty string "".

# works, 13.87th percentile for runtime, 79.5th for memory
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        for s in strs:
            if pref == "": return pref
            if len(s) < len(pref): pref = pref[:len(s)]
            for l_in in range(len(s)):
                if l_in >= len(pref):
                    break
                if s[l_in] != pref[l_in]:
                    pref = pref[:l_in]
                    break
        return pref
