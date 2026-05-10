class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = set() # (idx, num, curr)

        def dfs(i, curr):
            if i == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            
            res = 0
            if (i, nums[i]) not in dp:
                res += dfs(i + 1, curr + nums[i])
                res += dfs(i + 1, curr + nums[i] * -1)
                dp.add((i, nums[i], curr + nums[i]))
                dp.add((i, nums[i], curr - nums[i]))
                return res
            
            return 0
        
        return dfs(0, 0)
