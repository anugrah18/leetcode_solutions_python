class Solution:
    def canCompleteCircuit(self,gas,cost):

        total_cost = curr_cost = start_pos = 0

        for i in range(0,len(gas)):
            total_cost = total_cost + gas[i]-cost[i]
            curr_cost = curr_cost + gas[i]-cost[i]

            if(curr_cost<0):
                curr_cost = 0
                start_pos = i+1

        return start_pos if total_cost >=0 else -1


X = Solution()
print(X.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))

# Time Complexity : O(N)
# Space Complexity : O(1)
