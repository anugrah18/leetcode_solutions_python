class Solution(object):
    def decodeString(self, s):
        stack = []
        curr = ""
        count = 0

        for c in s:
            if(c == "["):
                stack.append((count,curr))
                count = 0
                curr = ""
            elif(c == "]"):
                (_count,_curr) = stack.pop()
                curr = _curr + (_count*curr)
            elif(c.isnumeric()):
                count = 10*count + int(c)
            else:
                curr = curr + c
        return curr

X = Solution()
print(X.decodeString("3[a2[c]]"))

# Time Complexity : O(N) , N= total number of characters
# Space Complexity : O(N)

