class Solution:
    def hammingWeight(self, n):
        res = 0
        # Loop until all bits are processed
        while n:
            # Add the least significant bit (0 or 1) to the result
            res += n % 2
            # Right shift the bits of n to process the next bit
            n = n >> 1
        return res
X = Solution()
print(X.hammingWeight(11))

# Time Complexity : O(LogN) , N = integer whose bits are to be counted
# Space Complexity : O(1)