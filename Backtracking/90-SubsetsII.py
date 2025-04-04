class Solution:
    def subsetsWithDup(self, nums):
        res = []  # Final result list to store all unique subsets
        nums.sort()  # Sort the list to group duplicates together

        # Helper function to perform backtracking
        def backtrack(i, subset):
            # Base case: if we've considered all elements
            if i == len(nums):
                res.append(subset.copy())  # Add a copy of the current subset
                return

            # Include the current element
            subset.append(nums[i])
            backtrack(i + 1, subset)  # Recurse to the next index with current element included
            subset.pop()  # Backtrack: remove the element

            # Skip duplicates
            # If the next number is the same as the current one, skip it to avoid duplicate subsets
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude the current element
            backtrack(i + 1, subset)  # Recurse to the next index with current element excluded

        backtrack(0, [])  # Start backtracking from index 0 with an empty subset
        return res  # Return the list of unique subsets


X = Solution()
print(X.subsetsWithDup([1, 2, 2]))

# Time Complexity : O(n*2^n)
# Space Complexity : O(n*2^n)
