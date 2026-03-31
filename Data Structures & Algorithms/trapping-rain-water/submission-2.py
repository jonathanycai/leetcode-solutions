class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        l, r = 0, len(height) - 1
        max_left = max_right = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= max_left:
                    max_left = height[l]
                else:
                    count += max_left - height[l]
                l += 1
            else:
                if height[r] >= max_right:
                    max_right = height[r]
                else:
                    count += max_right - height[r]
                r -= 1
        
        return count