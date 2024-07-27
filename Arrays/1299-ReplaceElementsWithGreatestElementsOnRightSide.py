class Solution:
    def replaceElements(self, arr):
        # Initialize the answer array with zeros
        ans = [0] * len(arr)
        # Initialize max_el to negative infinity
        max_el = -float('inf')

        # Iterate over the array from the second last element to the first element
        for i in range(len(arr) - 1, 0, -1):
            # Update max_el to be the maximum of max_el and the current element
            max_el = max(max_el, arr[i])
            # Set the element at the previous index in the answer array to max_el
            ans[i - 1] = max_el

        # Set the last element of the answer array to -1
        ans[-1] = -1

        # Return the answer array
        return ans

X = Solution()

print(X.replaceElements([17,18,5,4,6,1]))

# Time Complexity : O(N)
# Space Complexity : O(1)