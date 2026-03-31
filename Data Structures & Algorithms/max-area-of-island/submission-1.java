class Solution {
    
    int[][] grid;
    boolean[][] visited;
    
    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        this.visited = new boolean[grid.length][grid[0].length];
        int currBest = 0;

        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[0].length; col++) {
                int curr = search(row, col);
                currBest = Math.max(curr, currBest);
            }
        }

        return currBest;
    }

    public int search(int row, int col) {
        if (row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || visited[row][col] || grid[row][col] == 0) {
            return 0;
        }

        visited[row][col] = true;
        return search(row + 1, col) + search(row - 1, col) + search(row, col + 1) + search(row, col - 1) + 1;
    }
}
