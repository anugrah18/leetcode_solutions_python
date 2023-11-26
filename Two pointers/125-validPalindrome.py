class Solution(object):
    def isPalindrome(self, s):
        # Initialize an empty string to store the alphanumeric characters in lowercase
        alphaNumericString = ""

        # Iterate through each character in the input string
        for c in s:
            if (c.isalnum()):
                # Append the lowercase alphanumeric character to the string
                alphaNumericString = alphaNumericString + c.lower()

        # Calculate the length of the alphanumeric string
        N = len(alphaNumericString)

        # Iterate through the first half of the alphanumeric string
        for i in range(0, int(N / 2)):
            if (alphaNumericString[i] != alphaNumericString[N - i - 1]):
                # If not equal, the string is not a palindrome
                return False
        # If the loop completes without returning, the string is a palindrome
        return True

X = Solution()
print(X.isPalindrome("A man, a plan, a canal: Panama"))

# Time Complexity : O(N)
# Space Complexity : O(N)