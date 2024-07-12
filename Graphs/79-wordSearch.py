class Solution:
    def exist(self, board, word):
        # Iterate through each cell in the board
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                # Check if the current cell matches the first letter of the word
                # and start a DFS search from there
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):
                    return True

        # If no matching path is found, return False
        return False

    def dfs(self, board, i, j, count, word):
        # If all characters are matched, return True
        if count == len(word):
            return True

        # If the current position is out of bounds or does not match the character, return False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[count]:
            return False

        # Temporarily mark the board cell as visited
        temp = board[i][j]
        board[i][j] = "#"

        # Perform DFS in all four possible directions
        found = (self.dfs(board, i + 1, j, count + 1, word) or
                 self.dfs(board, i - 1, j, count + 1, word) or
                 self.dfs(board, i, j + 1, count + 1, word) or
                 self.dfs(board, i, j - 1, count + 1, word))

        # Restore the cell's original value
        board[i][j] = temp

        return found


X = Solution()
print(X.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))

# Time Complexity : O(M*N*4^L) , M = num of rows , N = num of columns , L = length of word
# Space Complexity : O(L)