class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                return ans;
            } else if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1;
            int right = nums.length - 1;
            int currNum = nums[i];
            while (left < right) {
                int leftVal = nums[left];
                int rightVal = nums[right];

                if (currNum + leftVal + rightVal < 0) {
                    left++;
                } else if (currNum + leftVal + rightVal > 0) {
                    right--;
                } else {
                    ans.add(Arrays.asList(currNum, leftVal, rightVal));
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                }
            }
        }

        return ans;
    }
}
