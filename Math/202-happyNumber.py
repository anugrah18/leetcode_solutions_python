def getNext(n):
    totalSum = 0  # Variable to store the sum of squares of digits
    while n > 0:
        n, digit = divmod(n, 10)  # Extract the last digit and reduce the number
        totalSum = totalSum + digit ** 2  # Square the digit and add to sum
    return totalSum  # Return the computed sum


class Solution(object):

    def isHappy(self, n):
        ht = set()  # Set to store seen numbers and detect loops
        while n != 1:  # Continue until we reach 1
            ht.add(n)  # Store the current number to detect cycles
            n = getNext(n)  # Get the next number in sequence
            if n in ht:  # If we see the same number again, it's a cycle
                return False  # Not a happy number

        return True  # If we reach 1, it's a happy number


# Example usage
X = Solution()
print(X.isHappy(19))  # Expected output: True (19 is a happy number)

# Time Complexity : O(logN)
# Space Complexity : O(logN)