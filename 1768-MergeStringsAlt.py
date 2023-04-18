# 1768. Merge Strings Alternately

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order,
# starting with word1. If a string is longer than the other,
# append the additional letters onto the end of the merged string.
# Return the merged string.

# works, runtime up to at least 93.19th percentile
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         new = ""
#         for l in range(min(len(word1), len(word2))):
#             new += word1[0] + word2[0]
#             word1 = word1[1:]
#             word2 = word2[1:]
#         new += word1 + word2
#         return new

# # works, memory up to at least 95.89th percentile
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         new = ""
#         r = min(len(word1), len(word2))
#         for l in range(r):
#             new += word1[l] + word2[l]
#         new += word1[r:] + word2[r:]
#         return new

# # works, runtime can be pretty good, fairly high memory usage
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         new = ""
#         r = min(len(word1), len(word2))
#         for l in range(r):
#             new = new + word1[l] + word2[l]
#         new = new + word1[r:] + word2[r:]
#         return new

# works, medium-slow runtime, pretty good memory
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        while word1 != "" and word2 != "":
            new = new + word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        new = new + word1 + word2
        return new