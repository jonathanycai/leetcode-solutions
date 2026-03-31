class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegree = [0] * (len(edges) + 1)
        adj = [[] for _ in range(len(edges) + 1)]

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            indegree[a] += 1
            indegree[b] += 1

        q = deque()
        for i, val in enumerate(indegree):
            if val == 1:
                q.append(i)

        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        q.append(nei)
        
        for a, b in reversed(edges):
            if indegree[a] > 1 and indegree[b] > 1:
                return [a, b]

        return []

