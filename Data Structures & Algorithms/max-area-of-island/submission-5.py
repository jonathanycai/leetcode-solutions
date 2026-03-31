class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxSize = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    print(r)
                    print(c)
                    size = self.dfs(r, c, grid)
                    maxSize = max(maxSize, size)

        return maxSize

        
    def dfs(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 0
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid[r][c] = 0
        res = 1
        for dr, dc in directions:
            res += self.dfs(r + dr, c + dc, grid)
        
        return res