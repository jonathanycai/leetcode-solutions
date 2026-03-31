class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        boolean visited[][] = new boolean[grid.length][grid[0].length];
        int maxVal = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                int currVal = search(grid, visited, i, j);
                maxVal = Math.max(currVal, maxVal);
            }
        }

        return maxVal;
    }

    private int search(int[][] grid, boolean[][] visited, int row, int col) {
        if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || visited[row][col] || grid[row][col] == 0) {
            return 0;
        }

        visited[row][col] = true;
        return search(grid, visited, row + 1, col) + search(grid, visited, row, col - 1) + search(grid, visited, row - 1, col) + search(grid, visited, row, col+ 1) + 1;
    }
}
