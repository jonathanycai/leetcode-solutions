class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        prevRow = [0] * n

        for r in range(m - 1, -1, -1):
            curRow = [0] * n

            # handle last column
            if obstacleGrid[r][n - 1] == 1:
                curRow[n - 1] = 0
            elif r == m - 1:
                curRow[n - 1] = 1
            else:
                curRow[n - 1] = prevRow[n - 1]

            for c in range(n - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                else:
                    curRow[c] = curRow[c + 1] + prevRow[c]

            prevRow = curRow

        return prevRow[0]