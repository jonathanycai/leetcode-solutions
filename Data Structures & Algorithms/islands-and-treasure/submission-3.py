class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
        
        dist = 1
        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if (newR >= 0 and newC >= 0 and 
                        newR < ROWS and newC < COLS and grid[newR][newC] == INF):
                        grid[newR][newC] = dist
                        q.append([newR, newC])
            dist += 1
        

                    
        