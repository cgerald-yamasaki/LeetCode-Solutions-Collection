# 2405 Optimal Partition of String

# Given a string s, partition the string into one or more substrings
# such that the characters in each substring are unique. That is,
# no letter appears in a single substring more than once.
# Return the minimum number of substrings in such a partition.
# Note that each character should belong to exactly one substring in a partition.

# works, 94.85th percentile runtime, 90.9th for memory
class Solution:
    def partitionString(self, s: str) -> int:
        if s == "": return 0
        used_set = set()
        ss_count = 0    # number of finished substrings
        for c in s:
            if c in used_set:
                ss_count += 1
                used_set = {c}
            else:
                used_set.add(c)
        return ss_count + 1