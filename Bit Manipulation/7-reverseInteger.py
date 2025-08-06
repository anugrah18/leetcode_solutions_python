class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        res = 0              # This will store the reversed number
        negative = x < 0     # Track whether input is negative
        x = abs(x)           # Work with positive value for now

        while x != 0:
            digit = x % 10   # Extract the last digit
            x //= 10         # Remove last digit from x

            # Check for potential overflow **before** multiplying/resizing
            # If res > INT_MAX // 10, any further multiplication would overflow
            # If res == INT_MAX // 10, adding a digit > 7 would overflow (because INT_MAX ends in 7)
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return 0     # Return 0 on overflow

            # Safe to proceed: multiply res by 10 and add the new digit
            res = res * 10 + digit

        # If the original number was negative, return -res
        return -res if negative else res

X = Solution()
print(X.reverse(123))

# Time Complexity : O(logN) - to base 10
# Space Complexity : O(1)