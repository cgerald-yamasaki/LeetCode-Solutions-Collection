# Sort an Array

# Given an array of integers nums, sort the array in ascending order
# and return it.
# You must solve the problem without using any built-in functions in
# O(nlog(n)) time complexity and with the smallest space complexity possible.

# Merge sort:
# works but is slow and uses a lot of memory.
# 11.34th percentile for runtime, 12.8th for memory
class Solution:
    def split(self, nums: List[int], split_lists: List[List[int]]) -> None:
        last = len(nums) - 1
        if last > 0:
            mid = (last) // 2
            Solution.split(self, nums[:mid + 1], split_lists)
            Solution.split(self, nums[mid + 1:], split_lists)
        else:
            split_lists.append([nums[0]])
    def sortArray(self, nums: List[int]) -> List[int]:
        split_lists = []
        Solution.split(self, nums, split_lists)
        split_lists_len = len(split_lists)
        while split_lists_len > 1:
            if split_lists_len % 2 == 1:
                split_lists_last = split_lists.pop()
            else: split_lists_last = None
            new_split_lists = []
            for pair_in in range(0, split_lists_len - 1, 2):
                merged_pair = []
                while split_lists[pair_in] != [] and split_lists[pair_in + 1] != []:
                    if split_lists[pair_in][0] <= split_lists[pair_in + 1][0]:
                        merged_pair.append(split_lists[pair_in].pop(0))
                    else:
                        merged_pair.append(split_lists[pair_in + 1].pop(0))
                if split_lists[pair_in] != []:
                    for el in split_lists[pair_in]:
                        merged_pair.append(el)
                elif split_lists[pair_in + 1] != []:
                    for el in split_lists[pair_in + 1]:
                        merged_pair.append(el)
                new_split_lists.append(merged_pair)
            if split_lists_last: new_split_lists.append(split_lists_last)
            split_lists = new_split_lists
            split_lists_len = len(split_lists)
        return split_lists[0]    