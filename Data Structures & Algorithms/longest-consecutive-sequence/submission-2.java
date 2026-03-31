class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num : nums) {
            set.add(num);
        }

        int best = 0;
        for (int num : nums) {
            int curr = 1;
            int temp = num;
            if (set.contains(num - 1)) {
                continue;
            }
            while (set.contains(temp + 1)) {
                curr++;
                temp++;
            }

            best = Math.max(best, curr);

        }

        return best;
    }
}
