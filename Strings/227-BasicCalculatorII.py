class Solution:
    def calculate(self, s: str) -> int:
        # Initialize pointers and variables to store current, previous values,
        # result, and current operation
        i = 0
        curr = prev = res = 0
        curr_operation = "+"

        # Iterate through the string
        while i < len(s):
            curr_char = s[i]

            # If the current character is a digit
            if curr_char.isdigit():
                # Construct the full number (in case it's more than one digit)
                while i < len(s) and s[i].isdigit():
                    curr = curr * 10 + int(s[i])
                    i += 1
                i -= 1  # Step back one index since the outer loop also increments `i`

                # Perform the operation based on the current operation sign
                if curr_operation == "+":
                    res += curr
                    prev = curr
                elif curr_operation == "-":
                    res -= curr
                    prev = -curr
                elif curr_operation == "*":
                    res -= prev  # Remove the previous value from the result
                    res += prev * curr  # Multiply and add the product to the result
                    prev = curr * prev  # Update `prev` to the product
                else:
                    res -= prev  # Remove the previous value from the result
                    res += int(prev / curr)  # Divide and add the quotient to the result
                    prev = int(prev / curr)  # Update `prev` to the quotient

                curr = 0  # Reset `curr` for the next number

            # If the current character is an operator (and not a space)
            elif curr_char != " ":
                curr_operation = curr_char  # Update the current operation

            i += 1  # Move to the next character

        return res


X = Solution()
print(X.calculate("3+2*2"))

# Time Complexity : O(N)
# Space Complexity : O(1)