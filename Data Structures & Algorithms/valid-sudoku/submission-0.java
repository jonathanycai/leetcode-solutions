class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        // check row
        for (int i = 0; i < board.length; i++) {
            Set<Character> seen = new HashSet<>();
            for (int j = 0; j < board[i].length; j++) {
                char item = board[i][j];
                if (item == '.') {
                    continue;
                } else if (seen.contains(item)) {
                    return false;
                }
                seen.add(item);
            }
        }

        // check col
        for (int i = 0; i < board[0].length; i++) {
            Set<Character> seen = new HashSet<>();
            for (int j = 0; j < board.length; j++) {
                char item = board[j][i];
                if (item == '.') {
                    continue;
                } else if (seen.contains(item)) {
                    return false;
                }
                seen.add(item);
            }
        }

        // check box
        for (int square = 0; square < 9; square++) {
            Set<Character> seen = new HashSet<>();
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') continue;
                    if (seen.contains(board[row][col])) return false;
                    seen.add(board[row][col]);
                }
            }
        }

        return true;
        

    }
}
