class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        target = sum(nums) // 2

        def dfs(i, curr):
            if i >= len(nums):
                return False
            
            if curr == target:
                return True
            elif curr > target:
                return False
            
            res = False
            if (i, curr) not in dp:
                res |= dfs(i + 1, curr + nums[i])
                res |= dfs(i + 1, curr)
                dp.add((i, curr))
                return res
            
            return False
        
        return dfs(0, 0)