# Collection of LeetCode Solutions

# Unless otherwise noted, each solution is my own.
# Started collecting them here 21 February 2023. 

# Single Element in a Sorted Array, LeetCode problem 540
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0   # start, end, and middle rep indices in nums
        end = len(nums) - 1
        middle = -1
        while start < end:
            middle = start + ((end - start) // 2)
            # print(start, middle, end)
            if nums[middle] == nums[middle - 1]:
                if (middle - 1 - start) % 2 == 1:
                    end = middle - 2
                else:
                    start = middle + 1
            elif nums[middle] == nums[middle + 1]:
                if (middle - start) % 2 == 1:
                    # print(start, middle, end)
                    end = middle - 1
                else:
                    start = middle + 2
            else:
                return nums[middle]
        return nums[start]