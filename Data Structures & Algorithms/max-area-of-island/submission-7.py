class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        maxSize = 0

        def dfs(r, c):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r, c) in seen or grid[r][c] == 0:
                return 0
            res = 1
            seen.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res
        
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in seen or grid[r][c] == 0:
                    continue
                res = max(res, dfs(r, c))

        return res