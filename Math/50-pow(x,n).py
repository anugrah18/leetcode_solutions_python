class Solution:
    def myPow(self, x, n):

        # Handle negative exponent by taking absolute value
        # If n is negative, we'll take the reciprocal of x at the end
        is_negative = n < 0
        n = abs(n)

        result = 1  # Initialize result as 1
        current_product = x  # Start with x as the base

        while n > 0:
            # If the current exponent bit is set (odd), multiply result by current product
            if n % 2 == 1:
                result *= current_product

            # Square the base (exponentiation by squaring)
            current_product *= current_product

            # Divide exponent by 2 (bitwise right shift)
            n //= 2

        # If the original exponent was negative, return the reciprocal
        return result if not is_negative else 1 / result


# Example usage:
X = Solution()
print(X.myPow(2.0, 10))

# Time Complexity : O(logN)
# Space Complexity : O(1)
