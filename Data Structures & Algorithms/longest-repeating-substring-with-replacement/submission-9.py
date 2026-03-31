class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxf = 0
        freq = defaultdict(int)
        res = float("-inf")

        while r < len(s):
            c = s[r]
            freq[c] += 1

            maxf = max(maxf, freq[c])

            while r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res