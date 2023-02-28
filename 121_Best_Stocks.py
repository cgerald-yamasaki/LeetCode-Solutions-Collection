# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a
# given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy
# one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

# slightly slower, distinctly worse memory
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         low = prices[0]     # index of lowest price so far
#         max_prof = 0    # largest difference between prices in order so far
#         prices_l = len(prices)
#         for i in range(prices_l):
#             curr_p = prices[i]
#             diff = curr_p - low
#             if diff > max_prof: max_prof = diff
#             if curr_p < low: low = curr_p
#         return max_prof

# works, 94.81th percentile for runtime, still 82.48th for memory
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]     # index of lowest price so far
        max_prof = 0    # largest difference between prices in order so far
        prices_l = len(prices)
        for i in range(prices_l):
            diff = prices[i] - low
            if diff > max_prof: max_prof = diff
            if prices[i] < low: low = prices[i]
        return max_prof

# works, 86.98th percentile for runtime, 82.48th for memory
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         low = prices[0]     # index of lowest price so far
#         max_prof = 0    # largest difference between prices in order so far
#         for i in range(len(prices)):
#             diff = prices[i] - low
#             if diff > max_prof: max_prof = diff
#             if prices[i] < low: low = prices[i]
#         return max_prof
            