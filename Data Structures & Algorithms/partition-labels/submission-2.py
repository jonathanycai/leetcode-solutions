class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i

        print(lastIndex)

        maxIdx = 0
        curr = 0
        res = []

        for i, c in enumerate(s):
            maxIdx = max(lastIndex[c], maxIdx)
            curr += 1
            if i == maxIdx:
                res.append(curr)
                curr = 0
        
        return res