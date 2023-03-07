# Minimum Time to Complete Trips

# You are given an array time where time[i] denotes the time taken
# by the ith bus to complete one trip.
# Each bus can make multiple trips successively; that is, the next
# trip can start immediately after completing the current trip.
# Also, each bus operates independently; that is, the trips of one
# bus do not influence the trips of any other bus.
# You are also given an integer totalTrips, which denotes the number
# of trips all buses should make in total. Return the minimum time
# required for all buses to complete at least totalTrips trips.

# works, p good runtime- 85th-95th percentile range
# really bad for memory- 5th percentile
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        shortest = min(time)
        max_time = totalTrips * shortest
        min_time = totalTrips // (shortest * len(time))
        trips = 0
        ret_time = max_time
        for t in time:
            trips += min_time // t
        if trips >= totalTrips: return min_time
        time_units = ((max_time - min_time) // 2) + min_time
        print(max_time, min_time)
        prev_try = min_time
        while time_units != prev_try :
            trips = 0
            for t in time:
                trips += time_units // t
            if trips >= totalTrips:
                max_time = time_units
                if time_units < ret_time: ret_time = time_units
            else: 
                min_time = time_units
            prev_try = time_units
            time_units = ((max_time - min_time) // 2) + min_time
            print(max_time, min_time)
        trips = 0
        ret_time -= 1
        for t in time:
            trips += ret_time // t
        if trips < totalTrips: return ret_time + 1
        else: return ret_time
