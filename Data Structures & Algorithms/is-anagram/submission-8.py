class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sFreq = {}
        tFreq = {}

        for i in range(len(s)):
            sFreq[s[i]] = sFreq.get(s[i], 0) + 1
            tFreq[t[i]] = tFreq.get(t[i], 0) + 1

        return sFreq == tFreq