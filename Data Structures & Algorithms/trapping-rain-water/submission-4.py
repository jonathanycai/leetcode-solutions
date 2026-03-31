class Solution:
    def trap(self, height: List[int]) -> int:
        tot = 0
        maxLeft, maxRight = 0, 0
        l, r = 0, len(height) - 1

        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= maxLeft:
                    maxLeft = height[l]
                else:
                    tot += maxLeft - height[l]
                l += 1
            else:
                if height[r] >= maxRight:
                    maxRight = height[r]
                else:
                    tot += maxRight - height[r]
                r -= 1
        
        return tot