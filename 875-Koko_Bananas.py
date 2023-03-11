# 875. Koko Eating Bananas

# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# works, very slow though
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles_len = len(piles)
        if piles_len == h:
            return max(piles)
        minimum = 1
        maximum = max(piles)
        k = (maximum - minimum) // 2 + minimum
        while k > minimum:
            hours1 = 0
            hours2 = 0
            for p in piles:
                hours1 += -(p // -k)
                hours2 += -(p // -(k - 1))
                if hours1 > h:
                    minimum = k + 1
                    k = (maximum - minimum) // 2 + minimum
                    break
            if hours1 > h: continue
            elif hours2 > h: return k
            maximum = k - 1
            k = (maximum - minimum) // 2 + minimum
        hours1 = 0
        for p in piles:
            hours1 += -(p // -k)
            if hours1 > h:
                return maximum
        return minimum
