class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) < n - 1:
            return False
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[b].append(a)
            adj[a].append(b)
        
        visited = set()
        def dfs(i, parent):
            if i in visited:
                return False
            visited.add(i)
            for n in adj[i]:
                if n == parent:
                    continue
                if not dfs(n, i):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
                