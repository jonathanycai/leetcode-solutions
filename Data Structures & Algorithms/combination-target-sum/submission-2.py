class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr, idx, total):
            if total == target:
                res.append(list(curr))
                return
            
            if idx >= len(nums) or total > target:
                return

            curr.append(nums[idx])
            dfs(curr, idx, total + nums[idx])
            curr.pop()
            dfs(curr, idx + 1, total)

        dfs([], 0, 0)

        return res