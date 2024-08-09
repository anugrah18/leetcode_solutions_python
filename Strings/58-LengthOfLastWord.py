class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Initialize the pointer (p) to the end of the string
        # Initialize length to 0, this will store the length of the last word
        p, length = len(s), 0

        # Traverse the string backwards
        while p > 0:
            # Move the pointer one step back
            p -= 1
            # If the current character is not a space, increase the length of the last word
            if s[p] != ' ':
                length += 1
            # If a space is encountered after finding some characters, return the length of the last word
            elif length > 0:
                return length

        # Return the length if the loop ends (handles cases with no spaces or trailing spaces)
        return length


# Example usage
X = Solution()
print(X.lengthOfLastWord("   fly me   to   the moon  "))

# Time Complexity : O(N)
# Space Complexity : O(1)
