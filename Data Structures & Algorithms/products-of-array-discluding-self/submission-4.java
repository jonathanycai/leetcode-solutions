class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] pre = new int[n];
        pre[0] = 1;

        for (int i = 1; i < nums.length; i++) {
            pre[i] = pre[i-1] * nums[i-1];
        }

        int post = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            pre[i] = post * pre[i];
            post *= nums[i];
        }

        return pre;
    }
}  
