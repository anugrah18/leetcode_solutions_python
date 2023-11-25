class Solution(object):
    def topKFrequent(self, words, k):
        dict = {}
        for word in words:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] = dict[word] + 1

        s = set(dict)
        s = sorted(s, key=lambda x: (-dict[x], x))
        return s[:k]


X = Solution()
print(X.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],
2))

# Time Complexity : O(NLogN)
# Space Complexity : O(N)