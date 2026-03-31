class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr, idx):
            if idx == len(nums):
                return
            
            if sum(curr) > target:
                return 
            elif sum(curr) == target:
                res.append(list(curr))
                return
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(curr, i)
                curr.remove(nums[i])

        dfs([], 0)

        return res