class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)

        for u, v in prerequisites:
            pre[v].append(u)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            
            if pre[crs] == []:
                return True
            
            visited.add(crs)
            for v in pre[crs]:
                if not dfs(v):
                    return False
            
            visited.remove(crs)
            pre[crs] = []
            return True

        for r in range(numCourses):
            if not dfs(r):
                return False
        
        return True