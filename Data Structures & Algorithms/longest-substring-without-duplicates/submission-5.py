class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLen = currLen = 0
        seen = defaultdict(int)

        while r < len(s):
            seen[s[r]] += 1
            
            while seen[s[r]] > 1:
                seen[s[l]] -= 1
                l += 1
                currLen -= 1
            
            r += 1
            currLen += 1
            maxLen = max(maxLen, currLen)

        return maxLen