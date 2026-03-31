class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, (x, y)))

        while k > 0:
            point = heapq.heappop(heap)
            res.append(point[1])
            k -= 1
        
        return res