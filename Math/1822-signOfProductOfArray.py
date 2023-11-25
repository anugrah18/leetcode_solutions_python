class Solution:
    def arraySign(self, nums):
        count = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                count += 1

        return 1 if count % 2 == 0 else -1


X= Solution()
print(X.arraySign([-1,-2,-3,-4,3,2,1]))