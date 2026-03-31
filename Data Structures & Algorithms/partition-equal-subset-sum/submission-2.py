class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        dp = set()
        target = sum(nums) // 2
        
        def dfs(i, curr):
            if i >= len(nums) or curr > target:
                return False
            if curr == target:
                return True

            res = False
            if (i, curr) not in dp:
                res |= dfs(i + 1, curr + nums[i]) 
                res |= dfs(i + 1, curr)
                dp.add((i, curr))
                return res
            
            return False
        
        return dfs(0, 0)
            