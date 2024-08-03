class Solution(object):
    def longestCommonPrefix(self, strs):
        # If the list is empty, return an empty string
        if len(strs) == 0:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Iterate through all strings in the list
        for i in range(1, len(strs)):
            # Reduce the prefix length until it matches the beginning of the current string
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                # If the prefix becomes empty, return an empty string
                if prefix == "":
                    return ""

        return prefix

X = Solution()
print(X.longestCommonPrefix(["flower", "flow", "flight"]))

# Time complexity : O(N*M) , where N = number of string, M = length of longest common prefix
# Space complexity : O(1)