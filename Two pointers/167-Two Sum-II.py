class Solution:
    def twoSum(self, numbers, target):

        L = 0  # Left pointer starts at the beginning of the list
        R = len(numbers) - 1  # Right pointer starts at the end of the list

        while L < R:
            current_sum = numbers[L] + numbers[R]  # Calculate the sum of two numbers

            if current_sum == target:
                # If sum matches the target, return the 1-based indices
                return [L + 1, R + 1]

            elif current_sum < target:
                # If sum is less than target, move left pointer to the right to increase sum
                L += 1

            else:
                # If sum is greater than target, move right pointer to the left to decrease sum
                R -= 1

X = Solution()
print(X.twoSum([2,3,4],6))

# Time Complexity: O(N)
# Space Complexity: O(1)
