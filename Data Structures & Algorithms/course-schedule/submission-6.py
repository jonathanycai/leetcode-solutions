class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finished = 0
        while q:
            crs = q.popleft()
            finished += 1
            for nei in adj[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finished == numCourses