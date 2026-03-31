class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int mLength = matrix.length;
        int col = matrix[0].length - 1;
        int row = 0;

        while (row < mLength && col >= 0) {
            if (matrix[row][col] < target) {
                row++;
            } else if (matrix[row][col] > target) {
                col--;
            } else {
                return true;
            }
        }

        return false;
    }
}
