class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check row
        for row in range(len(board)):
            curr_row = [x for x in board[row] if x != '.']
            if len(set(curr_row)) != len(curr_row):
                return False
        # Check col
        for col in range(len(board)):
            curr_col = [board[i][col] for i in range(9) if board[i][col] != '.']
            if len(set(curr_col)) != len(curr_col):
                return False
        
        # Check 9x9 grid
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                grid = [board[i+x][j+y] for x in range(3) for y in range(3) if board[i+x][j+y] != '.']
                if len(set(grid)) != len(grid):
                    return False
            
        
        return True