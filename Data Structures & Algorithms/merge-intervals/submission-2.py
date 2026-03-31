class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = [intervals[0]]

        for i in intervals[1 :]:
            start, end = i
            if start <= res[-1][1]:
                res[-1][0] = min(res[-1][0], start)
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(i)

        return res
