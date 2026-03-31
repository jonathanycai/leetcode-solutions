class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> index = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int sol = target - nums[i];
            if (index.containsKey(sol)) {
                int j = index.get(sol);
                if (j > i) {
                    return new int[]{i, j};
                } else {
                    return new int[]{j, i};
                }
            }

            index.put(nums[i], i);
        }

        return new int[2];
    }
}
