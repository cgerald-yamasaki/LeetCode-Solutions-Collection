# Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the
# first occurrence of needle in haystack, or -1 if needle is not
# part of haystack.

# works, gets somewhere between (ish) 98.68th and 66.84th percentile
# for runtime, and 54.39th and 10.97th for memory
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len = len(haystack)
        needle_len = len(needle)
        if needle_len > hay_len: return -1
        if needle[0] not in haystack: return -1
        for h_index in range(hay_len - (needle_len - 1)):
            for n_index in range(needle_len):
                if n_index == needle_len - 1 and haystack[h_index + n_index] == needle[n_index]:
                    return h_index
                if haystack[h_index + n_index] != needle[n_index]:
                    break
        return -1

# works, gets either 90.91st percentile or 78.97th for runtime..., 54.39th for memory
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         # index = -1
#         hay_len = len(haystack)
#         needle_len = len(needle)
#         if needle_len > hay_len: return -1
#         for h_index in range(hay_len - (needle_len - 1)):
#             for n_index in range(needle_len):
#                 if n_index == needle_len - 1 and haystack[h_index + n_index] == needle[n_index]:
#                     return h_index
#                 if haystack[h_index + n_index] != needle[n_index]:
#                     break
#         return -1