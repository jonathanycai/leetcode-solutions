class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return false;
        }

        HashMap<Character, Integer> s1Freq = new HashMap<>();
        for (char c : s1.toCharArray()) {
            s1Freq.put(c, s1Freq.getOrDefault(c, 0) + 1);
        }

        int need = s1Freq.size();
        for (int i = 0; i < s2.length(); i++) {
            HashMap<Character, Integer> s2Freq = new HashMap<>();
            int count = 0;
            for (int j = i; j < s2.length(); j++) {
                char c = s2.charAt(j);
                s2Freq.put(c, s2Freq.getOrDefault(c, 0) + 1);

                if (s1Freq.getOrDefault(c, 0) < s2Freq.get(c)) {
                    break;
                }

                if (s1Freq.getOrDefault(c, 0) == s2Freq.get(c)) {
                    count++;
                }

                if (count == need) {
                    return true;
                }
            }
        }

        return false;
    }
}
