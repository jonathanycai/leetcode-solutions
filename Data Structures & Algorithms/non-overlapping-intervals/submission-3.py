class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        latestEnd = intervals[0][1]
        count = 0

        for start, end in intervals[1 :]:
            if start < latestEnd:
                latestEnd = min(latestEnd, end)
                count += 1
            else:
                latestEnd = end
        
        return count
            