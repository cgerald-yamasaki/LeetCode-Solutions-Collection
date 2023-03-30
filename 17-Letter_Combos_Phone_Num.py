# Letter Combinations of a Phone Number

# Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

# works, 62.15th percentile for runtime, 66.39th for memory
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        num_map = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        working_list = []
        for l in num_map[int(digits[0]) - 2]:
            working_list.append(l)
        for d_in in range(1, len(digits)):
            new = []
            while working_list != []:
                pre = working_list.pop(0)
                for l in num_map[int(digits[d_in]) - 2]:
                    new.append(pre + l)
            working_list = new
        return working_list
