class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxf = 0
        seen = defaultdict(int)
        res = 0

        while r < len(s):
            seen[s[r]] += 1
            maxf = max(maxf, seen[s[r]])

            while (r - l + 1) -maxf > k:
                seen[s[l]] -= 1
                l += 1
            
            res = max(r - l + 1, res)
            r += 1
        
        return res