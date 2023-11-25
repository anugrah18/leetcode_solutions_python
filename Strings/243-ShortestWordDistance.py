class Solution:
    def shortestDistance(self, wordsDict, word1, word2):
        l1, l2 = -1, -1
        ans = float('inf')
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                l1 = i
            elif wordsDict[i] == word2:
                l2 = i
            if l1 != -1 and l2 != -1:
                ans = min(abs(l1 - l2), ans)

        return ans


X = Solution()
print(X.shortestDistance(["practice", "makes", "perfect", "coding", "makes"],"coding","practice"))


# Time Complexity : O(N)
# Space Complexity : O(1)