class Solution:
    def groupAnagrams(self, strs):
        res = []
        if len(strs) == 1:
            return [strs]

        ht = {}

        for s in strs:
            if ("".join(sorted(s))) not in ht:
                ht[("".join(sorted(s)))] = []

            ht[("".join(sorted(s)))].append(s)

        for key in ht:
            res.append(ht[key])

        return res
X = Solution()
print(X.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# Time Complexity : O(NKLogK) , N = length of strs , K = maximum length of string in strs
# Space Complexity : O(NK)