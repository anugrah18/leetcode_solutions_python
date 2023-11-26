class Solution:
    def twoSum(self, numbers, target):
        # Initialize the left pointer to the first element of the sorted list.
        ptr1 = 0
        # Initialize the right pointer to the last element of the sorted list.
        ptr2 = len(numbers) - 1

        while ptr1 < ptr2:
            # If the sum is greater than the target, move the right pointer to decrease the sum.
            if (numbers[ptr1] + numbers[ptr2]) > target:
                ptr2 -= 1
            # If the sum is less than the target, move the left pointer to increase the sum.
            elif (numbers[ptr1] + numbers[ptr2]) < target:
                ptr1 += 1
            # If the sum is equal to the target, return the indices of the two numbers with one base.
            else:
                return [ptr1 + 1, ptr2 + 1]


X = Solution()
print(X.twoSum([2,7,11,15],9))

# Time Complexity : O(N)
# Space Complexity : O(1)