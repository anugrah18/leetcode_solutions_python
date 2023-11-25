class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return
        stack = []
        ans = ""

        for c in s:
            if not stack or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()

        for i in range(len(stack)):
            ans += stack[i]

        return ans


X = Solution()
print(X.removeDuplicates("abbaca"))

# Time Complexity : O(N)
# Space Complexity : O(N)