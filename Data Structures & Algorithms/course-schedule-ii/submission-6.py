class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj =[[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        
        q = deque()
        for i, val in enumerate(indegree):
            if val == 0:
                q.append(i)
        res = []
        while q:
            length = len(q)
            for _ in range(length):
                crs = q.popleft()
                res.append(crs)
                for c in adj[crs]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        q.append(c)
        
        return res if len(res) == numCourses else []