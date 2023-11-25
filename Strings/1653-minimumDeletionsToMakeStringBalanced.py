from collections import Counter


class Solution:
    def minimumDeletions(self, s):
        dict = Counter(s)

        best = len(s)
        a = dict["a"]
        b = 0

        for x in s:
            best = min(best, b + a)
            if x == "a":
                a -= 1
            else:
                b += 1

        best = min(best, b + a)
        return best

X = Solution()
print(X.minimumDeletions("aababbab"))

# Time Complexity : O(N)
# Space Complexity : O(1)