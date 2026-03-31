class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, par):
            if node in visit:
                return
            
            visit.add(node)
            for n in adj[node]:
                if n == par:
                    continue
                dfs(n, node)

        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                res += 1

        return res