class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.word = False  # Boolean flag to indicate the end of a word

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Initialize the WordDictionary with a root node

    def addWord(self, word: str) -> None:
        curr = self.root  # Start from the root node
        for c in word:  # Iterate over each character in the word
            if c not in curr.children:  # If the character is not in the current node's children
                curr.children[c] = TrieNode()  # Add a new TrieNode as a child
            curr = curr.children[c]  # Move to the child node
        curr.word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root  # Start from the given node
            for i in range(j, len(word)):  # Iterate over each character in the word starting from index j
                c = word[i]
                if c == ".":  # If the character is a dot, it can match any character
                    for child in curr.children.values():  # Check all possible children nodes
                        if dfs(i + 1, child):  # Recursively search for the rest of the word
                            return True
                    return False  # If no match is found, return False
                else:
                    if c not in curr.children:  # If the character is not found in the current node's children
                        return False  # The word does not exist in the trie
                    curr = curr.children[c]  # Move to the child node
            return curr.word  # Return True if the current node marks the end of the word

        return dfs(0, self.root)  # Start the DFS traversal from the root and the first character of the word


wordDictionary = WordDictionary()
print(wordDictionary.addWord("bad"))
print(wordDictionary.addWord("dad"))
print(wordDictionary.addWord("mad"))
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))

# Time Complexity : O(N) , N = length of keys
# Space Complexity : O(N) , N = length of keys