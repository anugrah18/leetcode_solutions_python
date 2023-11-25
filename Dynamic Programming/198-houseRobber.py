class Solution(object):
    def rob(self,nums):
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        return dp[-1]

X =Solution()
houses = [2,7,9,3,1,7]
print(X.rob(houses))

# Time Complexity : O(N)
# Space Complexity : O(N)
