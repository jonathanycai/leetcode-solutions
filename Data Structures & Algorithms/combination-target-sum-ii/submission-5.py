class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, tot):
            if tot == target:
                res.append(curr.copy())
            
            if i >= len(candidates) or tot > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                curr.append(candidates[j])
                print(curr)
                dfs(j + 1, curr, tot + candidates[j])
                curr.pop()
        
        dfs(0, [], 0)

        return res