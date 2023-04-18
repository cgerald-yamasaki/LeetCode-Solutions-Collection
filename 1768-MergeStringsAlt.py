# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        r = min(len(word1), len(word2))
        for l in range(r):
            new = new + word1[l] + word2[l]
        new = new + word1[r:] + word2[r:]
        return new

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        while word1 != "" and word2 != "":
            new = new + word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        new = new + word1 + word2
        return new