class Solution:

    def permute(self, nums):
        if len(nums) < 2:
            return [nums]  # Base case: one element or empty → only one permutation

        ans = []
        for i, num in enumerate(nums):
            # Remove the current number and permute the rest
            for permutation in self.permute(nums[0:i] + nums[i + 1:]):
                # Prepend the fixed number to each permutation of the rest
                ans.append([num] + permutation)
        return ans


X = Solution()
print(X.permute([1, 2, 3]))

# Time complexity : O(n!)
# Space complexity : O(n!)
