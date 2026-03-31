class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int largest = 0;

        while (left < right) {
            int val = Math.min(heights[left], heights[right]) * (right - left);
            if (largest < val) {
                largest = val;
            }

            if (heights[left] < heights[right]) {
                left++;
            } else {
                right--;
            }
        }

        return largest;
    }
}
