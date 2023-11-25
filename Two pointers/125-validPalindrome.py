class Solution(object):
    def isPalindrome(self, s):
        alphaNumericString = ""

        for c in s:
            if (c.isalnum()):
                alphaNumericString = alphaNumericString + c.lower()
        N = len(alphaNumericString)

        for i in range(0, int(N / 2)):
            if (alphaNumericString[i] != alphaNumericString[N - i - 1]):
                return False

        return True

X = Solution()
print(X.isPalindrome("A man, a plan, a canal: Panama"))

# Time Complexity : O(N)
# Space Complexity : O(N)