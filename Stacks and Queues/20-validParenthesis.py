class Solution(object):
    def isValid(self, s):

        stack = []
        Dict = {')': '(', '}': '{', ']': '['}

        for c in s:

            if len(stack) > 0 and Dict.get(c) and Dict[c] == stack[len(stack)-1]:
                stack.pop()
            else:
                stack.append(c)

        if len(stack)==0:
            return True
        else:
            return False

X = Solution()
print(X.isValid("{(){}[]}"))

# Time Complexity : O(N)
# Space Complexity : O(N)
