class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1, res2 = [], []

        for c in s:
            if res1 and c == "#":
                res1.pop()
            else:
                if c != "#":
                    res1.append(c)

        for c in t:
            if res2 and c == "#":
                res2.pop()
            else:
                if c != "#":
                    res2.append(c)

        return res1 == res2

X = Solution()
print(X.backspaceCompare("ab#c","ad#c"))

# Time Complexity : O(M+N)
# Space Complexity : O(M+N)