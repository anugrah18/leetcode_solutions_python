class Solution(object):
    def numDecodings(self, s):
        # Initialize a dp array with zeros, with length one more than the input string
        dp = [0] * (len(s) + 1)
        # Base case: an empty string has one way to be decoded
        dp[0] = 1
        # If the first character is not '0', it can be decoded in one way
        if s[0] != "0":
            dp[1] = 1
        # Iterate over the string starting from the second character
        for i in range(2, len(s) + 1):
            # Check the last single digit
            one_digit = s[i - 1]
            if int(one_digit) > 0:
                # If it's a valid single digit, it contributes the same number of ways as dp[i-1]
                dp[i] = dp[i - 1]
            # Check the last two digits
            two_digit = s[i - 2:i]
            if int(two_digit) >= 10 and int(two_digit) <= 26:
                # If it's a valid two-digit number, add the ways from dp[i-2]
                dp[i] = dp[i] + dp[i - 2]
        # The last element in dp array contains the total number of ways to decode the string
        return dp[-1]


X = Solution()
print(X.numDecodings("125"))

# Time Complexity : O(N) , N = length of string
# Space Complexity : O(N)