class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, curr = -float("inf"), 0

        for n in nums:
            curr += n
            maxSum = max(curr, maxSum)
            if curr <= 0:
                curr = 0
        
        return maxSum
        