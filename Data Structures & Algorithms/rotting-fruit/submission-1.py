class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = deque()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while fresh > 0 and q:
            length = len(q)

            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc
                    if newR >= 0 and newR < ROWS and newC >= 0 and newC < COLS and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append((newR, newC))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
        