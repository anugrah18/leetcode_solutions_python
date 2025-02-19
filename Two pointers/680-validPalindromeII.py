class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize two pointers at the start and end of the string

        while l < r:  # Iterate until the two pointers meet
            if s[l] != s[r]:  # If characters at l and r do not match
                # Check if skipping one character (either left or right) makes the string a palindrome
                skipL, skipR = s[l + 1:r + 1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])  # Reverse and compare for palindrome check

            l += 1  # Move left pointer forward
            r -= 1  # Move right pointer backward

        return True  # If the loop completes, it's already a palindrome

# Test case
X = Solution()
print(X.validPalindrome("abca"))  # Output: True

# Time Complexity : O(N)
# Space Complexity : O(1)