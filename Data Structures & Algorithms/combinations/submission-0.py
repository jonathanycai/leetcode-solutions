class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(curr, start):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            for i in range(start, n + 1):
                curr.append(i)
                dfs(curr, i + 1)
                curr.pop()
        
        dfs([], 1)
        return res