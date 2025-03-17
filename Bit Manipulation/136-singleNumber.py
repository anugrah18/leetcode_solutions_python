class Solution(object):
    def singleNumber(self, nums):
        ans = 0  # Initialize a variable to store the unique number

        # Iterate through all numbers in the list
        for n in nums:
            ans = ans ^ n  # Apply XOR operation

            # XOR properties:
            # 1. a ^ a = 0 (same numbers cancel each other out)
            # 2. a ^ 0 = a (XOR with 0 keeps the number unchanged)
            # 3. XOR is commutative and associative (order does not matter)

        return ans  # The result will be the unique number


# Example usage
X = Solution()
series = [1, 2, 1, 2, 4, 3, 3]  # All numbers appear twice except for 4
print(X.singleNumber(series))  # Expected output: 4
