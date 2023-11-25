class Solution(object):
    def plusOne(self, digits):

        i = len(digits) - 1
        carry = 1
        while (i >= 0):

            sum = int((digits[i] + carry) % 10)
            carry = int((digits[i] + carry) / 10)
            digits[i] = sum

            if (carry == 0):
                return digits
            i = i - 1

        digits.insert(0, carry)
        return digits

X =Solution()
print(X.plusOne([9,9]))


# Time complexity : O(N)
# Space complexity : O(1)