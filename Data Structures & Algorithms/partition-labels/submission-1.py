class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        size = 0
        maxSoFar = lastIndex[s[0]]
        for i, c in enumerate(s):
            size += 1
            maxSoFar = max(lastIndex[c], maxSoFar)
            if i == maxSoFar:
                res.append(size)
                size = 0
        
        return res