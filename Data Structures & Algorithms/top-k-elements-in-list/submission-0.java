class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i = 0; i < freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int num : nums) {
            if (count.get(num) == null) {
                count.put(num, 0);
            }
            count.put(num, count.get(num) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        int[] ans = new int[k];
        int index = 0;
        for (int i = freq.length - 1; i >= 0; i--) {
            if (index == k) {
                break;
            }
            for(int j : freq[i]) {
                ans[index] = j;
                index++;
            }
        }
        return ans;
    }
}
