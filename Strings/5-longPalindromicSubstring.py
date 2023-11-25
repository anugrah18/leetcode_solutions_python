class Solution:
    _resStart = 0
    _resLength = 0

    def longestPalindrome(self,s):
        for i in range(0,len(s)):
            # Expand around a single character as the middle of the palindrome
            self._expandFromMiddle(s,i,i)
            # Expand around two characters as the middle of the palindrome
            self._expandFromMiddle(s,i,i+1)

        return s[self._resStart:self._resStart+self._resLength]

    def _expandFromMiddle(self,s,left,right):

        while(left>=0 and right<len(s) and s[left]==s[right]):
            # Expand as long as the characters at the left and right indices are the same
            left = left-1
            right = right+1

        if(self._resLength<right-left-1):
            # If the expanded palindrome is longer than the current longest palindrome
            self._resStart = left + 1
            self._resLength = right-left-1

X = Solution()
print(X.longestPalindrome("bhdbabbajnfjnfg"))


# Time Complexity : O(N^2)
# Space Complexity : O(1)

