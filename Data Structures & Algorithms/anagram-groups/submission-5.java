class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();

        for (String s : strs) {
            char[] freq = new char[26];
            for (char c : s.toCharArray()) {
                freq[c - 'a']++;
            }

            String key = Arrays.toString(freq);
            if (groups.get(key) == null) {
                groups.put(key, new ArrayList<>());
            }
            groups.get(key).add(s);
        }

        return new ArrayList<>(groups.values());
    }
}
