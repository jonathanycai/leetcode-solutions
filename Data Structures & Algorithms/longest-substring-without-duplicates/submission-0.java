class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> seenChar = new HashSet<>();
        int l = 0;
        int length = 0;

        for (int r = 0; r < s.length(); r++) {
            while (seenChar.contains(s.charAt(r))) {
                seenChar.remove(s.charAt(l));
                l++;
            }
            seenChar.add(s.charAt(r));
            length = Math.max(length, r - l + 1);
        }
        return length;
    }
}
