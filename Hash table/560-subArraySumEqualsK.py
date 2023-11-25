class Solution(object):
    def subarraySum(self, nums, k):
        dict = {}
        sum = 0
        result = 0

        dict[0] = 1
        for num in nums:
            sum = sum + num
            if ((sum - k) in dict):
                result = result + dict[sum - k]
            if (sum in dict):
                dict[sum] = dict[sum] + 1
            else:
                dict[sum] = 1
        return result

X =Solution()
print(X.subarraySum([1,2,5,-2,-5,7,8],8))

# Time Complexity : O(N)
# Space Complexity : O(N)