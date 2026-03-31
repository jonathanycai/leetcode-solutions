class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0;
        int r = numbers.length - 1;
        int[] ans = new int[2];

        while (l < r) {
            int sol = numbers[l] + numbers[r];

            if (sol < target) {
                l++;
            } else if (sol > target) {
                r--;
            } else if (sol == target) {
                ans[0] = l + 1;
                ans[1] = r + 1;
                break;
            }
        }
        return ans;
    }
}
