class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = l = r = 0
        
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(i + nums[i], furthest)
            l = r + 1
            r = furthest
            ans += 1
        
        return ans