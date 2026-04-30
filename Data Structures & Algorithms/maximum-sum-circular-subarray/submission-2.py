class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMin = globMax = nums[0]
        currMax = currMin = 0
        tot = sum(nums)

        for n in nums:
            currMax += n
            currMin += n
            print(currMin)
                
            globMin = min(globMin, currMin)
            globMax = max(globMax, currMax)

            if currMax < 0:
                currMax = 0
            if currMin > 0:
                currMin = 0
        
        return globMax if globMax < 0 else max(globMax, tot - globMin) 
