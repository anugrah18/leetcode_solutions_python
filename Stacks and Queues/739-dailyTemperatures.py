class Solution:

    def dailyTemperatures_I(self,T):
        # From front
        ans =[0]*len(T)
        stack =[]

        for i,t in enumerate(T):
            while stack and t>stack[-1][0]:
                temp,ind = stack.pop()
                ans[ind] = i-ind
            stack.append([t,i])

        return ans




    def dailyTemperatures_II(self,T):
        # From behind
        ans =[0]*len(T)
        stack =[]

        for i in range(len(T)-1,-1,-1):
            while(stack and T[i]>=T[stack[-1]]):
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

X = Solution()
print(X.dailyTemperatures_I([73,74,75,71,69,72,76,73]))
print(X.dailyTemperatures_II([73,74,75,71,69,72,76,73]))

# Time Complexity : O(N)
# Space Complexity : O(N)