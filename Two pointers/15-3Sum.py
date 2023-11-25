class Solution(object):
    def threeSum(self, nums):
        ans = set()
        nums.sort()

        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                if (nums[i] + nums[j] + nums[k] == 0):
                    ans.add((nums[i], nums[j], nums[k]))
                    j = j + 1
                    k = k - 1
                elif (nums[i] + nums[j] + nums[k] < 0):
                    j = j + 1
                elif (nums[i] + nums[j] + nums[k] > 0):
                    k = k - 1
        return ans

X = Solution()
print(X.threeSum([-1,0,1,2,-1,-4]))

# Time Complexity : O(N)
# Space Complexity : O(N)