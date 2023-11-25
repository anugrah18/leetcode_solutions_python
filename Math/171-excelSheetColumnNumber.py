class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(0, len(s)):
            sum = sum * 26 + (ord(s[i]) - ord('A') + 1)

        return sum


X =Solution();
colStr = "AZ"
print(X.titleToNumber(colStr))