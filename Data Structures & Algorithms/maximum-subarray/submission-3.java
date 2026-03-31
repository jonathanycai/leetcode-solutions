class Solution {
    public int maxSubArray(int[] nums) {
        int currMax = nums[0];
        int curr = 0;

        for (int i = 0; i < nums.length; i++) {
            curr = Math.max(curr, 0);

            curr += nums[i];
            currMax = Math.max(currMax, curr);
        }

        return currMax;
    }
}
