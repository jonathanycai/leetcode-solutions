class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(list), defaultdict(list), defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num in rows[r] or num in cols[c] or num in boxes[(r // 3, c // 3)]:
                    return False
                
                if num == '.':
                    continue
                
                rows[r].append(num)
                cols[c].append(num)
                boxes[(r // 3, c // 3)].append(num)
        
        return True
