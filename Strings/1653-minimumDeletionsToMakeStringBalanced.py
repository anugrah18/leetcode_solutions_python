class Solution:
    def minimumDeletions(self, s: str) -> int:
        ht = {}

        for c in s:
            ht[c] = ht.get(c, 0) + 1

        a = ht.get('a', 0)
        b = 0
        ans = len(s)

        for c in s:
            ans = min(ans, a + b)
            if c == 'a':
                a -= 1
            else:
                b += 1

        ans = min(ans, a + b)

        return ans


X = Solution()
print(X.minimumDeletions("aababbab"))

# Time Complexity : O(N)
# Space Complexity : O(N)