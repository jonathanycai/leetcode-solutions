class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, curr, tot):
            if tot == target:
                res.append(curr.copy())
                return
            
            if tot > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                curr.append(candidates[j])
                dfs(j + 1, curr, tot + candidates[j])
                curr.pop()
        
        dfs(0, [], 0)
        return res