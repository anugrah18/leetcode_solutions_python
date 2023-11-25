class Solution:
    def RemoveDuplicates_I(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        ans = ""
        for x in stack:
            ans += x[0] * x[1]

        return ans

    def RemoveDuplicates_II(self,s,k):
        stack = []
        i = 0

        while(i<len(s)):
            if(i==0 or s[i]!=s[i-1]):
                stack.append(1)
            if(stack[-1]==k):
                stack.pop()
                s = s[0:i-k+1]+s[i+1:]
                i = i-k
            else:
                stack[-1]+=1
            i+=1
        return s

X = Solution()
print(X.RemoveDuplicates_I("deeedbbcccbdaa",3))
print(X.RemoveDuplicates_II("deeedbbcccbdaa",3))

# Time Complexity : O(N)
# Space Complexity : O(N)