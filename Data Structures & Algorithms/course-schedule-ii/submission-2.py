class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)
        res = []
        
        for u, v in prerequisites:
            pre[u].append(v)

        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for req in pre[crs]:
                if not dfs(req):
                    return False
            
            
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res