class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCount = {}
        tCount = {}
        for num in range(len(s)):
            sCount[s[num]] = sCount.get(s[num], 0) + 1
            tCount[t[num]] = tCount.get(t[num], 0) + 1

        return sCount == tCount
            

        