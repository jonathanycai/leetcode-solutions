class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        maxL, curr = 0, 0
        l = 0

        for c in s:
            count[c] += 1
            curr += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
                curr -= 1
            
            maxL = max(maxL, curr)
        
        return maxL

