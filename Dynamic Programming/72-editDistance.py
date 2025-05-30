class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize DP cache with dimensions (len(word1)+1) x (len(word2)+1), filled with infinity initially
        cache = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # Base case: Fill the last row, representing deletion of characters from word2
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        # Base case: Fill the last column, representing deletion of characters from word1
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # Iterate backwards through both words
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # If characters match, no operation is needed, move diagonally
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    # If characters don't match, take minimum of insert, delete, or replace operations
                    cache[i][j] = 1 + min(
                        cache[i + 1][j],  # Delete operation
                        cache[i][j + 1],  # Insert operation
                        cache[i + 1][j + 1]  # Replace operation
                    )

        # Final answer is in the top-left cell, representing min distance for full words
        return cache[0][0]

X = Solution()
print(X.minDistance("intention","execution"))

# Time Complexity : O(M*N) , where M = len(word1) N = len(word2)
# Space Complexity : O(M*N)
