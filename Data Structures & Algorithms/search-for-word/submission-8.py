class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, i):
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != word[i] or board[r][c] == '#':
                return False

            if i == len(word) - 1:
                return True
            
            board[r][c] = '#'
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            found = False
            for dr, dc in directions:
                found = found or dfs(r + dr, c + dc, i + 1)
            
            board[r][c] = word[i]

            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False

