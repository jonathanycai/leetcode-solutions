class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, prev, ocean):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in ocean or heights[r][c] < prev:
                return
            
            ocean.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], ocean)
        
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        res = set()
        for r, c in pacific:
            if (r, c) in atlantic:
                res.add((r, c))
        
        return list(res)
