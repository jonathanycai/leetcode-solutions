class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> count1 = new HashMap<>();
        Map<Character, Integer> count2 = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            count1.put(s.charAt(i), count1.getOrDefault(s.charAt(i), 0) + 1);
            count2.put(t.charAt(i), count2.getOrDefault(t.charAt(i), 0) + 1);
        }

        return count1.equals(count2);
    }
}
