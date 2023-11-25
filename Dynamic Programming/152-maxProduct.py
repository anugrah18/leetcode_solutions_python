class Solution:
    def maxProduct(self,nums):

        if(len(nums)==0):
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1,len(nums)):
            curr = nums[i]
            temp_max = max(curr,curr*max_so_far,curr*min_so_far)
            min_so_far = min(curr,curr*max_so_far,curr*min_so_far)

            max_so_far = temp_max
            result = max(max_so_far,result)

        return result

X = Solution()
print(X.maxProduct([2,3,-2,4]))

# Time Complexity : O(N)
# Space Complexity : O(1)

