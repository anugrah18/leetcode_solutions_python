class Solution:
    count = 0

    def countSubstrings(self, s):
        for i in range(len(s)):
            # Expand around a single character as the middle of the palindrome
            self.expandFromMiddle(s, i, i)
            # Expand around two characters as the middle of the palindrome
            self.expandFromMiddle(s, i, i + 1)
        return self.count

    def expandFromMiddle(self, s, i, j):
        while (i >= 0 and j < len(s) and s[i] == s[j]):
            # Expand as long as the characters at the left and right indices are the same
            self.count += 1
            i -= 1
            j += 1

X =Solution()
print(X.countSubstrings("abc"))

# Time Complexity : O(N)
# Space Complexity: O(1)
