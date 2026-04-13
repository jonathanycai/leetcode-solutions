class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        tot = 0
        res = float("inf")

        while r < len(nums):
            tot += nums[r]

            while tot >= target and l <= r:
                res = min(r - l + 1, res)
                tot -= nums[l]
                l += 1
            
            r += 1
        
        return res if res != float("inf") else 0
            
            