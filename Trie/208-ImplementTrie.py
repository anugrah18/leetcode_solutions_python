class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.endOfWord = False  # Boolean flag to indicate the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the trie with a root node

    def insert(self, word: str) -> None:
        curr = self.root  # Start from the root node
        for c in word:  # Iterate over each character in the word
            if c not in curr.children:  # If the character is not in the current node's children
                curr.children[c] = TrieNode()  # Add a new TrieNode as a child
            curr = curr.children[c]  # Move to the child node
        curr.endOfWord = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        curr = self.root  # Start from the root node
        for c in word:  # Iterate over each character in the word
            if c not in curr.children:  # If the character is not found
                return False  # The word does not exist in the trie
            curr = curr.children[c]  # Move to the child node
        return curr.endOfWord  # Return True if the current node marks the end of the word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root  # Start from the root node
        for c in prefix:  # Iterate over each character in the prefix
            if c not in curr.children:  # If the character is not found
                return False  # The prefix does not exist in the trie
            curr = curr.children[c]  # Move to the child node
        return True  # If all characters in the prefix are found, return True

trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))

# Time Complexity : O(N) , N = length of keys
# Space Complexity : O(N) , N = length of keys
