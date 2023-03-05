# Count Subarrays With Fixed Bounds

# You are given an integer array nums and two integers minK and maxK.
# A fixed-bound subarray of nums is a subarray that satisfies the
# following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.

# straight up from someone else's posted solution, middle of the road for runtime and memory
# translated to python3 from C and I added the first if but almost exactly
#  singhabhinash's solution, I DID NOT COME UP WITH THIS
# class Solution:
#     def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         if minK not in nums or maxK not in nums: return 0
#         nums_len = len(nums)
#         leftBound = -1
#         lastMin = -1
#         lastMax = -1
#         count = 0
#         for i in range(nums_len):
#             if nums[i] >= minK and nums[i] <= maxK:
#                 if nums[i] == minK: lastMin = i
#                 if nums[i] == maxK: lastMax = i
#                 count += max(0, min(lastMin, lastMax) - leftBound)
#             else:
#                 leftBound = i
#                 lastMin = -1
#                 lastMax = -1
#         return count

    
    
    
    # returns indices of smallest isolated min-max pairs in nums
        bases = []
        base_min = None
        base_max = None
        for i in range(nums_len):
            if nums[i] == minK:
                if base_max != None:
                    bases.append([base_max, i])
                    base_min = None
                    base_max = None
                else:
                    base_min = i
            if nums[i] == maxK:
                if base_min != None:
                    bases.append([base_min, i])
                    base_min = None
                    base_max = None
                else:
                    base_max = i
        print(bases)
        return bases
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        if minK not in nums or maxK not in nums: return 0
        nums_len = len(nums)
        if nums_len == 2: return 1
        bases = Solution.getBases(self, nums, minK, maxK, nums_len)
        if bases == []: return 0
        count = 0
        if minK == maxK:
            series_count = 1
            bases_len = len(bases)
            for base_in in range(1, bases_len):
                if bases[base_in - 1][0] == bases[base_in][0] - 1 and base_in != bases_len - 1:
                    series_count += 1
                else:
                    if base_in == bases_len - 1 and bases[base_in - 1][0] == bases[base_in][0] - 1:
                        series_count += 1
                    print(series_count)
                    for c in range(series_count):
                        count += c + 1
                    series_count = 1
            return count
        for base in bases:
            count += 1
            i = base[0] - 1
            while i >= 0 and nums[i] != nums[base[1]] and nums[i] >= minK and nums[i] <= maxK:
                count += 1
                i -= 1
            j = base[1] + 1
            while j < nums_len and nums[j] != nums[base[0]] and nums[j] >= minK and nums[j] <= maxK:
                count += 1
                j += 1
        return count
        
        count = 0
        incrementer = 1
        min_done = False
        max_done = False
        prev_min = None
        prev_max = None
        nums_len = len(nums)
        for i in nums_len:
            if nums[i] < minK or nums[i] > maxK:
                min_done = False
                max_done = False
                print(nums[i], min_done, max_done)
                continue
            if nums[i] == minK:
                if min_done:
                    if max_done and prev_max > prev_min:
                        count += prev_max - prev_min
                min_done = True
                if max_done and min_done:
                    count += prev_max - prev_min
                prev_min = i
                print(nums[i], "min_done")
            if nums[i] == maxK:
                max_done = True
                print(nums[i], "max_done")
            if nums[i] >= minK and nums[i] <= maxK and min_done and max_done:
                count += 1
                print(nums[i], count)
                # if min_done and max_done: count += 1
                # else: continue
        return count
        

        count = 0
        incrementer = 1
        min_done = False
        max_done = False
        prev_min = None
        prev_max = None
        nums_len = len(nums)
        for i in nums_len:
            if nums[i] < minK or nums[i] > maxK:
                min_done = False
                max_done = False
                print(nums[i], min_done, max_done)
                continue
            if nums[i] == minK:
                min_done = True
                if max_done and min_done:
                    count += prev_max - prev_min
                prev_min = i
                print(nums[i], "min_done")
            if nums[i] == maxK:
                max_done = True
                print(nums[i], "max_done")
            if nums[i] >= minK and nums[i] <= maxK and min_done and max_done:
                count += 1
                print(nums[i], count)
                # if min_done and max_done: count += 1
                # else: continue
        return count
        
        count = 0
        min_done = False
        max_done = False
        possible_c = 0
        for num in nums:
            if num < minK or num > maxK: # outside range
                min_done = False
                max_done = False
                possible_c = 0
                continue
            if num == minK:
                # if max_done == False: # catch this case in num >= minK?
                #     possible_c += 1
                if min_done == False and max_done == True: # first minK in this section
                    count += possible_c
                    possible_c = 0
                min_done = True
            if num == maxK:
                if max_done == False and min_done == True:
                    count += possible_c
                    possible_c = 0
                max_done = True
            if num >= minK and num <= maxK:
                if not min_done or not max_done:
                    possible_c += 1
                    continue
                else: count += 1
        return count
                
        
        
        count = 0
        min_done = False
        max_done = False
        for num in nums:
            if num < minK or num > maxK:
                min_done = False
                max_done = False
                print(num, min_done, max_done)
                continue
            if num == minK:
                min_done = True
                print(num, "min_done")
            if num == maxK:
                max_done = True
                print(num, "max_done")
            if num >= minK and num <= maxK and min_done and max_done:
                count += 1
                print(num, count)
                # if min_done and max_done: count += 1
                # else: continue
        return count
            

