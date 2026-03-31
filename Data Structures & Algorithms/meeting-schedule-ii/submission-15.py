"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x : x.start)
        heap = []
        heapq.heappush(heap, intervals[0].end)

        for i in intervals[1: ]:
            if i.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
        
        return len(heap)


        

