class Solution:
    def groupAnagrams(self, strs):

        # Edge case: if there is only one string in the input, return it as a single group
        if len(strs) == 1:
            return [strs]

        # Create a hash table to group strings by their sorted version
        ht = {}

        # Iterate over each string in the input list
        for s in strs:
            # Sort the characters of the string and use the sorted version as the key
            sorted_key = "".join(sorted(s))

            # If the sorted version is not already in the hash table, add it with an empty list
            if sorted_key not in ht:
                ht[sorted_key] = []

            # Append the original string to the list corresponding to its sorted key
            ht[sorted_key].append(s)

        # Return the list of groups of anagrams
        return list(ht.values())

# Create an instance of the Solution class
X = Solution()

# Test the function with a sample input and print the result
print(X.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Time Complexity : O(NKLogK), where N is the number of strings and K is the maximum length of a string in strs.
# Sorting each string takes O(KLogK), and we do it for all N strings.

# Space Complexity : O(NK), where we store all strings in the hash table, and K is the length of the string.
