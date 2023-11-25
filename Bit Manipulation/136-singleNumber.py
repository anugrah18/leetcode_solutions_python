class Solution(object):
    def singleNumber(self, nums):
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans


X= Solution()
series = [1,2,1,2,4,3,3]
print(X.singleNumber(series))