class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;
            if (map.get(diff) != null) {
                int j = map.get(diff);
                if (i < j) {
                    return new int[]{i, j};
                } else {
                    return new int[]{j, i};
                }
            }
            map.put(num, i);
        }

        return new int[2];
    }
}
