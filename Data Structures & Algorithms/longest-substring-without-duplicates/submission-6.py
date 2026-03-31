class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        seen = defaultdict(int)
        currMax = currLen = 0

        while r < len(s):
            seen[s[r]] += 1

            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1
                currLen -= 1
            
            r += 1
            currLen += 1
            currMax = max(currLen, currMax)

        return currMax
