class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map <String, List<String>> group = new HashMap<>();

        for (String s : strs) {
            int[] count = new int[26];
            
            for (char c : s.toCharArray()) {
                count[c - 'a']++;
            }

            String key = Arrays.toString(count);
            if (group.get(key) == null) {
                group.put(key, new ArrayList<>());
            }
            List<String> grouping = group.get(key);
            group.get(key).add(s);
        }
        return new ArrayList<>(group.values());
    }
}
