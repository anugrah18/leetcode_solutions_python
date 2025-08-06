class Solution:
    def partitionLabels(self, s):
        # Dictionary to store the last occurrence index of each character
        pos = {}
        for i in range(len(s)):
            # Update to the latest position of character s[i]
            pos[s[i]] = i

        max_part = 0  # Tracks the farthest index the current partition should go
        ans = []      # Stores the sizes of the partitions
        l = r = 0     # l = start of current partition, r = current character index

        while r < len(s):
            # Extend the current partition to include the last occurrence of s[r]
            max_part = max(max_part, pos[s[r]])

            # If we have reached the end of the current partition
            if r == max_part:
                # Add the length of this partition to the result
                ans.append(r - l + 1)
                # Start a new partition from the next character
                l = r + 1
            r += 1

        return ans


X =Solution()
print(X.partitionLabels("ababcbacadefegdehijhklij"))

# Time Complexity : O(N)
# Space Complexity : O(1)