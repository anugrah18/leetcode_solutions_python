class Solution(object):
    def trailingZeroes(self, n):
        zeroCount=0
        while(n>0):
            n = int(n/5)
            zeroCount = zeroCount + n
        return zeroCount

X= Solution()
print(X.trailingZeroes(25))