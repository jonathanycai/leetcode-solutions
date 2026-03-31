class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        res = []

        for idx, i in enumerate(intervals):
            
            start, end = i

            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[idx : ]
            elif newInterval[0] > end:
                res.append(i)
            else:
                newInterval = [
                    min(newInterval[0], start),
                    max(newInterval[1], end)
                ]
        
        res.append(newInterval)
        return res
