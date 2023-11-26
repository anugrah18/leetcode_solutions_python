class Solution(object):
    def threeSum(self, nums):
        # Use a set to store unique triplets
        ans = set()
        # Sort the array for efficient traversal
        nums.sort()

        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while (j < k):
                # Check if the current triplet sums up to zero
                if (nums[i] + nums[j] + nums[k] == 0):
                    # Add the triplet to the set
                    ans.add((nums[i], nums[j], nums[k]))
                    # Move the left pointer
                    j = j + 1
                    # Move the right pointer
                    k = k - 1
                elif (nums[i] + nums[j] + nums[k] < 0):
                    # If sum is less than zero, move the left pointer
                    j = j + 1
                elif (nums[i] + nums[j] + nums[k] > 0):
                    # If sum is greater than zero, move the right pointer
                    k = k - 1
        return ans

X = Solution()
print(X.threeSum([-1,0,1,2,-1,-4]))

# Time Complexity : O(N)
# Space Complexity : O(N)