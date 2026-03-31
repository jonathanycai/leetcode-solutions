class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr, idx):
            if idx == len(nums):
                return
            
            res.append(list(curr))

            for i in range(len(nums)):
                if i <= idx:
                    continue
                curr.append(nums[i])
                dfs(curr, i)
                curr.remove(nums[i])

        dfs([], -1)

        return res