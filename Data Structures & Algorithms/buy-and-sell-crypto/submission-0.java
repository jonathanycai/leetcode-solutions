class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int left = 0;
        int right = 1;

        while (right < prices.length) {
            if (prices[left] < prices[right]) {
                int calc = prices[right] - prices[left];
                if (profit < calc) {
                    profit = calc;
                }
            } else {
                left = right; // found a new lowest price
            }
            right++;
        }
        return profit;

    }
}
