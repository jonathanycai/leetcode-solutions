class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 1;
        int r = piles[0];
        for (int i = 0; i < piles.length; i++) {
            if (piles[i] > r) {
                r = piles[i];
            }
        }

        int time = r;
        while (l <= r) {
            int k = (l + r) / 2;
            int tot = 0;
            for (int p : piles) {
                tot += Math.ceil((double) p / k);
            }

            if (tot <= h) {
                time = k;
                r = k - 1;
            } else {
                l = k + 1;
            }
        }
        return time;
    }
}
