class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2**31 - 1
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        dist = 1
        while q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                for dr, dc in direction:
                    newR = dr + r
                    newC = dc + c
                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == INF:
                        grid[newR][newC] = dist
                        q.append((newR, newC))
            dist += 1
        