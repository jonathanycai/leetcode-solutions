class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> freq = new HashMap<>();
        int l = 0, maxFreq = 0, maxLength = 0;

        for (int r = 0; r < s.length(); r++) {
            freq.put(s.charAt(r), freq.getOrDefault(s.charAt(r), 0) + 1);
            maxFreq = Math.max(maxFreq, freq.get(s.charAt(r)));

            if ((r - l + 1) - maxFreq > k) {
                freq.put(s.charAt(l), freq.get(s.charAt(l)) - 1);
                l++;
            }

            maxLength = Math.max(maxLength, r - l + 1);
        }

        return maxLength;
    }
}
