class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int currBest = 0;

        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                int curr = search(grid, visited, row, col);
                currBest = Math.max(curr, currBest);
            }
        }

        return currBest;
    }

    private int search(int[][] grid, boolean[][] visited, int row, int col) {
        if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length ||
            visited[row][col] || grid[row][col] == 0) {
            return 0;
        }

        visited[row][col] = true;
        return 1 + search(grid, visited, row + 1, col)
                 + search(grid, visited, row - 1, col)
                 + search(grid, visited, row, col + 1)
                 + search(grid, visited, row, col - 1);
    }
}
