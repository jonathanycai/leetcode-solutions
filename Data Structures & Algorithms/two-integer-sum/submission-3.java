class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indices = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            indices.put(nums[i], i);
        }

        int[] ans = new int[2];
        int key;

        int difference = 0;
        for (int i = 0; i < nums.length; i++) {
            difference = target - nums[i];
            if (indices.containsKey(difference)) {
                key = indices.get(difference);
                if (i == key) {
                    continue;
                }
                if (key > i) {
                    ans[0] = i;
                    ans[1] = key;
                } else {
                    ans[0] = key;
                    ans[1] = i;
                }
                
            }
        }
        return ans;
    }
}
