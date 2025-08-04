class Solution:
    def canCompleteCircuit(self, gas, cost):
        # total_cost: net gas gain/loss across all stations
        # curr_cost: gas available in the current segment (between resets)
        # start_pos: index of the potential starting station
        total_cost = curr_cost = start_pos = 0

        # Iterate through all stations
        for i in range(len(gas)):
            # Net gas at this station: gas[i] - cost[i]
            total_cost += gas[i] - cost[i]
            curr_cost += gas[i] - cost[i]

            # If we can't reach the next station from current path
            if curr_cost < 0:
                # Start fresh from the next station
                curr_cost = 0
                start_pos = i + 1

        # If total gas is enough to cover total cost, return starting station
        # Otherwise, return -1 (not possible to complete the circuit)
        return start_pos if total_cost >= 0 else -1


X = Solution()
print(X.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))

# Time Complexity : O(N)
# Space Complexity : O(1)
