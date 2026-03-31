class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int bestVal = 0;

        while (left < right) {
            int currVal = (right - left) * Math.min(heights[left], heights[right]);

            bestVal = Math.max(currVal, bestVal);
            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return bestVal;
    }
}
