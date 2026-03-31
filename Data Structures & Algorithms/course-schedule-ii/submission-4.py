class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        
        q = deque()
        for idx, value in enumerate(indegree):
            if value == 0:
                q.append(idx)
        
        res = []
        while q:
            length = len(q)
            for _ in range(length):
                crs = q.popleft()
                res.append(crs)
                for nei in adj[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)

        return res if len(res) == numCourses else []

            
