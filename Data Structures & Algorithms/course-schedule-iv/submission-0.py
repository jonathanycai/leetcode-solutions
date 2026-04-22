class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        isPreReq = [set() for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre].add(crs)
            indegree[crs] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for n in adj[node]:
                isPreReq[n].add(node)
                isPreReq[n].update(isPreReq[node])
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        return [u in isPreReq[v] for u, v in queries]