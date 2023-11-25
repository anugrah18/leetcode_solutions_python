class Solution:
    def exist(self,board,word):
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if (board[i][j]==word[0] and self.dfs(board,i,j,0,word)):
                    return True

        return False


    def dfs(self,board,i,j,count,word):
        if count==len(word):
            return True

        if(i<0 or i>len(board)-1 or j<0 or j>len(board[i])-1 or board[i][j]!=word[count]):
            return False

        temp = board[i][j]
        board[i][j]="#"
        found = self.dfs(board,i+1,j,count+1,word) or self.dfs(board,i-1,j,count+1,word) or \
        self.dfs(board, i, j+1, count + 1, word) or self.dfs(board,i,j-1,count+1,word)

        board[i][j] = temp

        return found

X = Solution()
print(X.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))

# Time Complexity : O(MN) , MN = lenght of grid
# Space Complexity : O(L) , L = length of the word to be matched