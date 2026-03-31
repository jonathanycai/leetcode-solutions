class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length() ) {
            return false;
        }



        Map<Character, Integer> v1 = new HashMap<>(); // For string s
        Map<Character, Integer> v2 = new HashMap<>(); // For string t

        for (int i = 0; i < s.length(); i++) {
            v1.put(s.charAt(i), v1.getOrDefault(s.charAt(i), 0) + 1);
            v2.put(t.charAt(i), v2.getOrDefault(t.charAt(i), 0) + 1);
        }

        return v1.equals(v2);
    }
}
