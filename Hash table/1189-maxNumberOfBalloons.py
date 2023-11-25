class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b, a, l, o, n = 0, 0, 0, 0, 0

        for c in text:
            if (c == "b"):
                b += 1
            if (c == "a"):
                a += 1
            if (c == "l"):
                l += 1
            if (c == "o"):
                o += 1
            if (c == "n"):
                n += 1

        return min(b, a, l // 2, o // 2, n)

X = Solution()
print(X.maxNumberOfBalloons("loonbalxballpoon"))

# Time Complexity : O(N)
# Space Complexity : O(1)