class Solution:
    def isValidSudoku(self, board):
        # N = Number of rows and cols in sudoko board
        # M = Box identifier multipier
        N = 9
        M = 3

        cols = {}
        rows = {}
        squares = {}

        for i in range(N):
            cols[i] = []
            rows[i] = []
            squares[i] = []

        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                rows[r].append(board[r][c])
                if board[r][c] in cols[c]:
                    return False
                cols[c].append(board[r][c])
                if board[r][c] in squares[(r // M) * M + c // M]:
                    return False
                squares[(r // M) * M + c // M].append(board[r][c])

        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

X = Solution()
print(X.isValidSudoku(board))

# Time Complexity : O(N^2) , N = board length
# Space Complexity : O(N^2) , N = board length

