class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        l, r = 0, len(heights) - 1

        greatest = 0
        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            if curr > greatest:
                greatest = curr
            if heights[l] < heights[r]:
                l+=1
            else:
                r -= 1
        return greatest

        