class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        bestL, bestR = 0, 0

        for i in range(len(s)):
            l, r = self.isPali(s, i, i)

            if r - l > bestR - bestL:
                bestL = l
                bestR = r
            
            l, r = self.isPali(s, i, i + 1)

            if r - l > bestR - bestL:
                bestL = l
                bestR = r
        
        return s[bestL : bestR + 1]




    def isPali(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return (l + 1, r - 1)