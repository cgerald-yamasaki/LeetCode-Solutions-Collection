# Capacity To Ship Packages Within D Days

# A conveyor belt has packages that must be shipped from one port
# to another within days days.
# The ith package on the conveyor belt has a weight of weights[i].
# Each day, we load the ship with packages on the conveyor belt
# (in the order given by weights). We may not load more weight
# than the maximum weight capacity of the ship.

# Return the least weight capacity of the ship that will result in
# all the packages on the conveyor belt being shipped within days days.

# works but very slow, 77.72nd percentile for memory though
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        ave = sum(weights) // days
        capacity = max(weights)
        if ave > capacity: capacity = ave
        num_weights = len(weights)
        d = 0
        w_index = 0
        while True:
            while d < days:
                sum_weight = 0
                while sum_weight <= capacity:
                    if w_index >= num_weights: return capacity
                    sum_weight += weights[w_index]
                    w_index += 1
                w_index -= 1
                d += 1
            capacity += 1
            d = 0
            w_index = 0

