class Solution:
    def reverseBits(self, n):
        res = 0
        # Iterate over each bit position from 0 to 31
        for i in range(32):
            # Extract the i-th bit from n
            bit = (n >> i) & 1
            # Set the (31 - i)-th bit in res
            res = res | (bit << (31 - i))

        return res

X = Solution()
print(X.reverseBits(43261596))

# Time Complexity : O(1)
# Space Complexity: O(1)