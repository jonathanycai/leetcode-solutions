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
        heap = [intervals[0].end]

        for i in intervals[1 :]:
            if i.start < heap[-1]:
                if heap[0] <= i.start:
                    heapq.heappop(heap)
                heapq.heappush(heap, i.end)
        
        print(heap)
        return len(heap)
