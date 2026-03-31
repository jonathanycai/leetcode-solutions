class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = []

        for task in count.values():
            heapq.heappush(heap, -task)
        
        q = deque() # (count, time)
        time = 0

        while q or heap:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(heap)
                if count:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time