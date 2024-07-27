class Solution:

    def tictactoe(self, moves) -> str:
        n = 3  # Size of the Tic-Tac-Toe board
        rows, cols = [0] * n, [0] * n  # Track the sum of moves for each row and column
        d1, d2 = 0, 0  # Track the sum of moves for the two diagonals
        player = 1  # Player 1 is represented by 1 and Player 2 by -1

        for r, c in moves:
            rows[r] += player  # Add the player's value to the row sum
            cols[c] += player  # Add the player's value to the column sum
            if r == c:
                d1 += player  # If the move is on the main diagonal, add the player's value to d1
            if r + c == n - 1:
                d2 += player  # If the move is on the anti-diagonal, add the player's value to d2

            # Check if the absolute value of any row, column, or diagonal sum is equal to n
            if abs(rows[r]) == n or abs(cols[c]) == n or abs(d1) == n or abs(d2) == n:
                if player == 1:
                    return "A"  # Player 1 wins
                else:
                    return "B"  # Player 2 wins

            player *= -1  # Switch player

        # If all moves have been made and no winner, check if the game is a draw or pending
        if len(moves) == (n * n):
            return "Draw"  # All cells are filled and no winner
        else:
            return "Pending"  # There are still moves to be made

X = Solution()
print(X.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))

# Time Complexity : O(m) , m = length of moves
# Space Complexity : O(n) , n = length of board