class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store the count of characters in the current window
        count = {}

        # Variable to store the result (length of the longest substring with the same characters)
        res = 0

        # Two pointers, 'l' and 'r', representing the left and right boundaries of the current window
        l = 0

        # Iterate through the string using the right pointer 'r'
        for r in range(len(s)):
            # Update the count of the current character in the window
            count[s[r]] = 1 + count.get(s[r], 0)

            # Check if the length of the current window minus the count of the most frequent character
            # is greater than the allowed replacements 'k'
            while (r - l + 1) - max(count.values()) > k:
                # Decrease the count of the character at the left boundary 'l'
                count[s[l]] -= 1
                # Move the left boundary 'l' forward
                l += 1

            # Update the result with the maximum length of the current valid substring
            res = max(res, r - l + 1)

        # Return the final result
        return res


X = Solution()
print(X.characterReplacement("ABAB",2))

# Time Complexity : O(n)
# Space complexity : O(m) m = number of unique characters