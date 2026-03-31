class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == '#' or board[r][c] != word[i]:
                return False
            
            board[r][c] = '#'
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            good = False
            for dr, dc in directions:
                good |= dfs(i + 1, r + dr, c + dc)
            
            board[r][c] = word[i]

            return good
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        
        return False
