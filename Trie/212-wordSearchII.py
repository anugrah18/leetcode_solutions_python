class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.isWord = False  # Boolean flag to indicate the end of a word

    def addWord(self, word):
        curr = self  # Start from the current TrieNode
        for c in word:  # Iterate over each character in the word
            if c not in curr.children:  # If the character is not in the current node's children
                curr.children[c] = TrieNode()  # Add a new TrieNode as a child
            curr = curr.children[c]  # Move to the child node
        curr.isWord = True  # Mark the end of the word

class Solution:
    def findWords(self, board, words):
        root = TrieNode()  # Initialize the trie with a root node
        for w in words:  # Add all words to the trie
            root.addWord(w)
        ROWS, COLS = len(board), len(board[0])  # Number of rows and columns in the board

        res, visit = set(), set()  # Initialize result set and visited set

        def dfs(r, c, node, word):
            # Base case: if out of bounds or already visited or character not in current node's children
            if (r < 0 or c < 0 or
                    r == ROWS or
                    c == COLS or
                    (r, c) in visit or
                    board[r][c] not in node.children):
                return
            visit.add((r, c))  # Add current cell to visited set
            node = node.children[board[r][c]]  # Move to the child node
            word += board[r][c]  # Append current character to the word
            if node.isWord:  # If the current node marks the end of a word
                res.add(word)  # Add the word to the result set
            # Recursively search in all four directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))  # Remove current cell from visited set

        for r in range(ROWS):  # Iterate over each cell in the board
            for c in range(COLS):
                dfs(r, c, root, "")  # Start DFS from each cell

        return list(res)  # Return the result as a list



X= Solution()
print(X.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"]))

# Time Complexity : O(N*M*4^L) , Where L is length of word, N = num of rows, M = num of cols
# Space Complexity: O(N*L)