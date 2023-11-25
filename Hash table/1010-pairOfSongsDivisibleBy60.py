class Solution:
    def numPairsDivisibleBy60_I(self,time):
        dict = {}
        res = 0
        dict[0] = 0

        for t in time:
            rem = t % 60

            if not rem:
                res += dict[0]
                dict[0] += 1
            else:
                if 60 - rem in dict:
                    res += dict[60 - rem]
                dict[rem] = dict.get(rem, 0) + 1

        return res



    def numPairsDivisibleBy60_II(self,time):
        dict = {}
        res = 0

        for t in time:
            if ((60-t)%60) not in dict:
                dict[(60-t)%60]=0
            if t%60 not in dict:
                dict[t%60] = 0

            res += dict[(60-t)%60]
            dict[t%60]+=1

        return res

X = Solution()
print(X.numPairsDivisibleBy60_I([30,20,150,100,40]))
print(X.numPairsDivisibleBy60_I([30,20,150,100,40]))

# Time Complexity : O(N)
# Space Complexity : (1)
