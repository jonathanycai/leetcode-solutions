class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        print(stones)
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if y < x:
                x -= y
                heapq.heappush(stones, -x)
            
        
        return -stones[0] if stones else 0