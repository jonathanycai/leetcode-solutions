class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        int[] soln = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (map.containsKey(diff) && map.get(diff) != i) {
                if (i < map.get(diff)) {
                    soln[0] = i;
                    soln[1] = map.get(diff);
                } else {
                    soln[0] = map.get(diff);
                    soln[1] = i;
                }
            }
        }
        return soln;
    }
}
