class Solution:
    def solve(self, board):
        """
        Modifies the given board in-place.
        Captures all 'O's that are fully surrounded by 'X's.
        'O's on the border or connected to the border are safe and should not be captured.
        """

        ROWS, COLS = len(board), len(board[0])

        # Step 1: DFS to mark 'O's connected to borders with a temporary marker 'T'
        def capture(r, c):
            # Base case: out of bounds or not an 'O'
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"  # Temporarily mark as not to be captured
            # Recurse on 4 neighboring directions
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 2: Start DFS from border cells to mark safe 'O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # Step 3: Flip all remaining 'O' to 'X' (captured), restore 'T' back to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  # Captured
                elif board[r][c] == "T":
                    board[r][c] = "O"  # Safe, revert back


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
X = Solution()
X.solve(board)
print(board)

# Time Complexity : O(MN)
# Space Complexity : O(MN)
