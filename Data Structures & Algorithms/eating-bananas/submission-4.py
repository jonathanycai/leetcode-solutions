class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            rate = l + (r - l) // 2
            time = 0

            for p in piles:
                time += math.ceil(float(p) / rate)
            
            if time <= h:
                res = rate
                r = rate - 1
            else:
                l = rate + 1
        
        return res