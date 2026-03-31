class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;

        while (l <= r) {
            int mid = l + (r - l) / 2;
            int midVal = nums[mid];

            if (midVal < target) {
                l = mid + 1;
            } else if (midVal > target) {
                r = mid - 1;
            } else {
                return mid;
            }
        }

        return -1;
    }
}
