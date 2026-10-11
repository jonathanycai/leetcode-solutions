class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        maximum, minimum = 1, 1

        for n in nums:
            temp = maximum * n
            maximum = max(n, maximum * n, minimum * n)
            minimum = min(n, temp, minimum * n)

            res = max(maximum, res)
        
        return res