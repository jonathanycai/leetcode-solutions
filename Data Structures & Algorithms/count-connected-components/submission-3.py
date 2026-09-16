class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited= set()

        def dfs(i):
            visited.add(i)
            for n in adj[i]:
                if n in visited:
                    continue
                dfs(n)
        
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res