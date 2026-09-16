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
            length = len(q)
            for _ in range(length):
                crs = q.popleft()
                finished += 1
                for c in adj[crs]:
                    indegree[c] -= 1
                    if indegree[c] == 0:
                        q.append(c)
    
        
        return finished == numCourses

        