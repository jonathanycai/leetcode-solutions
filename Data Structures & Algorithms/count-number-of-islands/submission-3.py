class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.dfs(r, c, grid)
                    res += 1
        
        return res


    def dfs(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or  grid[r][c] == "0":
            return
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        grid[r][c] = "0"
        for dr, dc in directions:
            self.dfs(r + dr, c + dc, grid)
