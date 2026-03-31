class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        dependencies = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            inDegree[a] += 1
            dependencies[b].append(a)

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        res = []
        finished = 0
        while q:
            crs = q.popleft()
            finished += 1
            res.append(crs)

            for n in dependencies[crs]:
                inDegree[n] -= 1
                if inDegree[n] == 0:
                    q.append(n)

        return res if finished == numCourses else []