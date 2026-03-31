class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currMax = -1
        l, r = 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            dist = r - l
            amt = dist * height
            currMax = max(amt, currMax)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return currMax