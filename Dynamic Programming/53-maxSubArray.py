class Solution(object):
    def maxSubArray(self, nums):

        maxSum = nums[0]
        currentSum  = nums[0]
        i = 1
        while(i<len(nums)):
            if(nums[i]>currentSum+nums[i]):
                currentSum = nums[i]
            else:
                currentSum = currentSum + nums[i]
            maxSum = currentSum if currentSum > maxSum else maxSum
            i = i+1
        return maxSum


X = Solution()
ans = X.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

print(ans)

# Time Complexity : O(N)
# Space Complexity : O(1)

