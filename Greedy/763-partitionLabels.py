class Solution:
    def partitionLabels(self, s):
        pos = {}

        for i in range(len(s)):
            if s[i] not in pos:
                pos[s[i]] = 0
            pos[s[i]] = i

        max_part = 0
        ans = []
        l = r = 0

        while r < len(s):
            max_part = max(max_part, pos[s[r]])
            if r == max_part:
                ans.append(r - l + 1)
                l = r + 1
            r += 1

        return ans

X =Solution()
print(X.partitionLabels("ababcbacadefegdehijhklij"))

# Time Complexity : O(N)
# Space Complexity : O(1)