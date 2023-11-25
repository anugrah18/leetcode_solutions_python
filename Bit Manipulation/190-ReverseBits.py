class Solution:
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res

X = Solution()
print(X.reverseBits(43261596))