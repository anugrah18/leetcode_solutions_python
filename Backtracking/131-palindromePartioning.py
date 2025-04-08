class Solution:
    def partition(self, s):
        res = []  # Final result: list of all valid palindrome partitions
        part = []  # Current partition being built

        # DFS helper to explore all partitions starting at index i
        def dfs(i):
            # Base case: if we've reached the end of the string, save the current partition
            if i >= len(s):
                res.append(part.copy())
                return

            # Try every possible substring starting at index i
            for j in range(i, len(s)):
                # Only proceed if s[i:j+1] is a palindrome
                if self.isPali(s, i, j):
                    # Include the palindrome in the current partition
                    part.append(s[i:j + 1])
                    # Recurse from the next index
                    dfs(j + 1)
                    # Backtrack: remove last added substring and try a different cut
                    part.pop()

        dfs(0)  # Start the DFS from index 0
        return res

    # Helper function to check if s[l:r] is a palindrome
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


X = Solution()
print(X.partition("aab"))

# Time Complexity : O(n * 2^n)
# Space Complexity : O(n * 2^n)
