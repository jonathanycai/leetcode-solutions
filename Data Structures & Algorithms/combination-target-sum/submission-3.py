class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr, i, tot):
            if tot == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or tot > target:
                return 0
            
            curr.append(nums[i])
            tot += nums[i]
            dfs(curr, i, tot)
            curr.pop()
            tot -= nums[i]
            dfs(curr, i + 1, tot)

        dfs([], 0, 0)
        return res