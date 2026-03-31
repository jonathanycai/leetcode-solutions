class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> word1 = new HashMap<>();
        char[] s1 = s.toCharArray();
        char[] s2 = t.toCharArray();

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            if (!word1.containsKey(s1[i])) {
                word1.put(s1[i], 1);
            } else {
                word1.put(s1[i], word1.get(s1[i]) + 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            if (word1.get(s2[i]) != null && word1.get(s2[i]) > 0) {
                word1.put(s2[i], word1.get(s2[i]) - 1);
            } else {
                return false;
            }
        }

        return true;
    }
}
