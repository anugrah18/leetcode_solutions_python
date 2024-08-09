class Solution:
    def shortestDistance(self, wordsDict, word1: str, word2: str) -> int:
        # Initialize indices for word1 (m) and word2 (n) to infinity
        # This helps in handling cases where one or both words have not been encountered yet
        m = float('inf')
        n = float('inf')

        # Initialize the answer (ans) to infinity
        # This will store the shortest distance between word1 and word2
        ans = float('inf')

        # Iterate through the words in the list with their indices
        for i, word in enumerate(wordsDict):
            # If the current word matches word1, update its index (m)
            if word == word1:
                m = i

            # If the current word matches word2, update its index (n)
            if word == word2:
                n = i

            # Update the shortest distance by comparing the current distance with the previous minimum
            ans = min(ans, abs(m - n))

        # Return the shortest distance found
        return ans


X = Solution()
print(X.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))

# Time Complexity : O(N) where N is the number of words in wordsDict
# Space Complexity : O(1) as the space used is constant, regardless of the input size
