class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of its digits (as strings)
        num = list(str(num))

        max_digit = "0"  # Track the maximum digit seen so far (from right to left)
        max_i = -1       # Index of the max_digit
        swap_i, swap_j = -1, -1  # Indices to swap for maximizing the number

        # Traverse digits from right to left
        for i in range(len(num)-1, -1, -1):
            # Update max_digit and its index if current digit is greater
            if num[i] > max_digit:
                max_digit = num[i]
                max_i = i
            # If current digit is less than the max seen so far, mark for swap
            elif num[i] < max_digit:
                swap_i, swap_j = i, max_i

        # Perform the swap if a beneficial one was found
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]

        # Convert list of digits back to integer and return
        return int("".join(num))

X = Solution()
print(X.maximumSwap(2736))

# Time Complexity : O(N) , N = number of digits
# Space COmplexity : O(N)