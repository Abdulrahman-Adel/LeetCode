class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
    
        while(l <= r):
            mid = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            if hours <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l