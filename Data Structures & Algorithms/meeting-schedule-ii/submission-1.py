"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key = lambda i: i.start)
        times = [intervals[0].end]

        for i in intervals[1 :]:
            start, end = i.start, i.end
            
            if start < times[-1]:
                if times[0] <= start:
                    heapq.heappop(times)
                heapq.heappush(times, end)

        return len(times)
        
