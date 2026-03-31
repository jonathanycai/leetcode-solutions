class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int l = 0;
        int r = matrix.length - 1;

        while (l <= r) {
            int index = (l + r) / 2;
            int endMatrix = matrix[index].length - 1;
            if (target >= matrix[index][0] && target <= matrix[index][endMatrix]) {
                int ml = 0;
                int mr = endMatrix;
                while (ml <= mr) {
                    int mIndex = (ml + mr) / 2;
                    int curr = matrix[index][mIndex];
                    
                    if (curr == target) {
                        return true;
                    } else if (target < curr) {
                        mr = mIndex -1;
                    } else {
                        ml = mIndex + 1;
                    }
                }
                return false;
            } else if (target < matrix[index][0]) {
                r = index - 1;
            } else {
                l = index + 1;
            }
        }

        return false;

    }
}
