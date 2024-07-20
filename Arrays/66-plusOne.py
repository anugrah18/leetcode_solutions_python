class Solution:
    def plusOne(self, digits):
        # Initialize carry to 1 because we are adding one to the number
        agg, carry = 0, 1

        # Iterate over the digits from the last to the first
        for i in range(len(digits) - 1, -1, -1):
            # Calculate the new value at the current position
            agg = (carry + digits[i]) % 10
            # Calculate the carry for the next position
            carry = (carry + digits[i]) // 10
            # Update the digit at the current position
            digits[i] = agg

        # If there is a carry left after the last digit, add it to the front
        return digits if carry == 0 else [carry] + digits


X =Solution()
print(X.plusOne([9,9]))


# Time complexity : O(N)
# Space complexity : O(1)