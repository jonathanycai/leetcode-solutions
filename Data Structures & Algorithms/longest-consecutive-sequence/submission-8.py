class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxL = 0

        for n in nums:
            if (n-1) in seen:
                continue
            
            num = n
            curr = 1
            while num + 1 in seen:
                curr += 1
                num += 1
            maxL = max(curr, maxL)
        
        return maxL