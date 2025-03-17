class Solution:
    def missingNumberI(self, nums) -> int:
        # Initialize res to the length of nums
        res = len(nums)

        # Calculate the expected sum of indices and actual sum of nums
        for i in range(len(nums)):
            res += (i - nums[i])

        return res

    def missingNumberII(self, nums) -> int:
        # Compute the expected sum of numbers from 0 to n using the sum formula
        # Sum of first n natural numbers: n * (n + 1) / 2
        n = len(nums)
        expect = (n * (n + 1)) // 2  # Expected total sum

        # Compute the actual sum of the numbers present in the list
        actual = 0
        for num in nums:
            actual += num  # Sum all the numbers in the given list

        # The missing number is the difference between the expected and actual sum
        return expect - actual


X = Solution()
print(X.missingNumberI([3,0,1]))
print(X.missingNumberII([3,0,1]))

# Time Complexity : O(N)
# Space Complexity : O(1)