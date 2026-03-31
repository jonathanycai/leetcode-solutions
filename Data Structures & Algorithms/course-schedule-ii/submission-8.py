class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        
        q = deque()
        for i, degree in enumerate(indegree):
            if degree == 0:
                q.append(i)
        
        res = []
        while q:
            length = len(q)
            for _ in range(length):
                crs = q.popleft()
                res.append(crs)
                for n in adj[crs]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        q.append(n)

        return res if len(res) == numCourses else []
        