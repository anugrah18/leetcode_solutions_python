class Solution:
    def findDuplicates(self, nums):
        # Initialize a set to store the duplicate numbers
        ans = set()

        # Iterate through each number in the list
        for n in nums:
            # If the number at the index abs(n)-1 is negative, it means the number n is a duplicate
            if nums[abs(n) - 1] < 0:
                # Add the absolute value of n to the set of duplicates
                ans.add(abs(n))
            else:
                # Otherwise, negate the number at the index abs(n)-1 to mark it as visited
                nums[abs(n) - 1] *= -1

        # Convert the set of duplicates to a list and return it
        return list(ans)

X = Solution()
print(X.findDuplicates([4,3,2,7,8,2,3,1]))


# Time Complexity : O(N)
# Space Complexity : O(N)