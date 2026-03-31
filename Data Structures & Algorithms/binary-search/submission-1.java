class Solution {
    public int search(int[] nums, int target) {
        int l = 0;
        int r = nums.length - 1;
        while (l <= r) {
            int index = (l + r) / 2;
            int curr = nums[index];
            if (curr == target) {
                return index;
            } else if (curr < target) {
                l = index + 1;
            } else {
                r = index - 1;
            }
        }
        return -1;
    }
}
