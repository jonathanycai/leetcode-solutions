class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        inDegree = [0] * (n + 1)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            inDegree[u] += 1
            inDegree[v] += 1

        q = deque()
        for i in range(1, n + 1):
            if inDegree[i] == 1:
                q.append(i)
        
        while q:
            node = q.popleft()
            inDegree[node] -= 1
            for n in adj[node]:
                inDegree[n] -= 1
                if inDegree[n] == 1:
                    q.append(n)
        
        for u, v in reversed(edges):
            if inDegree[u] > 0 and inDegree[v] > 0:
                return [u, v]
        
        return []