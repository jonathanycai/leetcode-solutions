class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxSize = 0

        for n in nums:
            if n - 1 in seen:
                continue
            size = 1
            copy = n
            while copy + 1 in seen:
                copy += 1
                size += 1
            maxSize = max(size, maxSize)
        
        return maxSize