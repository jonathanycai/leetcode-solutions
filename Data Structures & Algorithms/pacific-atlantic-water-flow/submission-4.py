class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(ocean, r, c, prevHeight):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevHeight or (r, c) in ocean:
                return
            
            ocean.add((r, c))
            for dr, dc in directions:
                dfs(ocean, r + dr, c + dc, heights[r][c])

        for r in range(ROWS):
            dfs(pacific, r, 0, -1)
            dfs(atlantic, r, COLS - 1, -1)

        for c in range(COLS):
            dfs(pacific, 0, c, -1)
            dfs(atlantic, ROWS - 1, c, -1)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
            
            
