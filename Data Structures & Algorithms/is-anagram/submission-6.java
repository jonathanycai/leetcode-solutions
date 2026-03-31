class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        
        Map<Character, Integer> seen1 = new HashMap<>();
        Map<Character, Integer> seen2 = new HashMap<>();

        char[] sChar = s.toCharArray();
        char[] tChar = t.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            seen1.put(sChar[i], seen1.getOrDefault(sChar[i], 0) + 1);
            seen2.put(tChar[i], seen2.getOrDefault(tChar[i], 0) + 1);
        }
        
        return seen1.equals(seen2);
    }
}
