class Solution {
    public int subarraySum(int[] nums, int k) {
        int res = 0;
        int currSum = 0;
        Map<Integer, Integer> prefix = new HashMap<>();
        prefix.put(0, 1);

        for (int num : nums) {
            currSum += num;
            int diff = currSum - k;
            res += prefix.getOrDefault(diff, 0);
            prefix.put(currSum, prefix.getOrDefault(currSum, 0) + 1);
        }

        return res;
    }
}