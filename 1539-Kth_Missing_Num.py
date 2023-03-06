# Kth Missing Positive Number

# Given an array arr of positive integers sorted in a strictly
# increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.

# works, 88.93rd percentile for runtime, 80.43rd for memory
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing_count = 0
        curr = 1
        for num in arr:
            while curr < num:
                missing_count += 1
                if missing_count == k:
                    return curr
                curr += 1
            curr += 1
        return curr + (k - missing_count - 1)