class Solution:

    def topKFrequent(self, nums, k):

        # Dictionary to store the frequency of each number
        ht = {}

        # Count occurrences of each number
        for num in nums:
            if num not in ht:
                ht[num] = 0  # Initialize the count if not present
            ht[num] += 1   # Increment the count

        # Get unique numbers from the dictionary keys
        unique = set(ht)

        # Sort unique numbers based on their frequency in descending order
        sorted_ans = sorted(unique, key=lambda x: -ht[x])

        # Return the top K elements
        return sorted_ans[:k]


# Example usage
X = Solution()
print(X.topKFrequent([1,1,1,2,2,3], 2))  # Expected output: [1, 2]

# Time Complexity : O(NLogN) where N = number of elements
# Space Complexity : O(N)