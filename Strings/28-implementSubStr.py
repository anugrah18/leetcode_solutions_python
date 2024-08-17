class Solution(object):
    #approach 1
    # Time Complexity : O((m-n)*n)
    # Space Complexity : O(1)
    def strStr(self, haystack, needle):
        if (needle == ""):
            return 0
        m = len(haystack)
        n = len(needle)

        if (m < n):
            return -1

        for i in range(0, m - n + 1):
            for j in range(0, n):
                if (haystack[i + j] != needle[j]):
                    break
                if (j == n - 1):
                    return i

        return -1

    # approach 2
    # Time Complexity : O((m-n)*n) , m=len(haystack)
    # Space Complexity : O(1)
    def strStr2(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i:i + len(needle)] == needle:
                    return i
            return -1

X = Solution()
print(X.strStr("liver","ve"))
print(X.strStr2("liver","ve"))

