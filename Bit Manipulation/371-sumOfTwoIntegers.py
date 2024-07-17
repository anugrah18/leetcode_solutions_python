class Solution:
    def getSum(self, a, b):
        # Define a mask to limit the integers to 32 bits (to handle overflow in Python)
        mask = 0xFFFFFFFF  # This is 2^32 - 1

        # Iterate until there is no carry left
        while b != 0:
            # Calculate sum without carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # Handle negative numbers by checking if a exceeds max positive 32-bit integer
        max_int = 0x7FFFFFFF  # This is 2^31 - 1 (largest positive 32-bit integer)
        return a if a < max_int else ~(a ^ mask)

X = Solution()
print(X.getSum(11,2))

# Time Complexity : O(1)
# Space Complexity : O(1)
