class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)

        for i, n in enumerate(nums):
            if n > 0:
                return res
            
            if i and nums[i - 1] == nums[i]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                tot = n + nums[l] + nums[r]

                if tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    res.append((n, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res
                    
