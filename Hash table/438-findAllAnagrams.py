class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            if p[i] not in pCount:
                pCount[p[i]] = 0
            pCount[p[i]] += 1
            if s[i] not in sCount:
                sCount[s[i]] = 0
            sCount[s[i]] += 1

        res = [0] if sCount == pCount else []

        l = 0
        for r in range(len(p), len(s)):
            if s[r] not in sCount:
                sCount[s[r]] = 0
            sCount[s[r]] += 1
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)

        return res

X = Solution()
print(X.findAnagrams("cbaebabacd","abc"))

# Time Complexity : O(N)
# Space Complexity : O(N)
