class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        # Zip combines two or more iterables.
        # Combine position and speed into a list of tuples
        pair = list(zip(position, speed))
        # Sort the list of tuples in descending order based on position
        pair.sort(reverse=True)

        # Stack to store time taken for each car to reach the target
        stack = []

        # Iterate through the sorted list of cars
        for p, s in pair:
            # Calculate the time needed for the current car to reach the target
            time_to_reach_target = (target - p) / s
            # Add the time to the stack
            stack.append(time_to_reach_target)
            # Check if there are at least two cars in the stack,
            # and if the current car takes less or equal time to reach the target
            # compared to the car in front (a faster car cannot catch up)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Remove the car in front (faster car cannot catch up)
                stack.pop()
        # The length of the stack represents the number of car fleets
        return len(stack)

X = Solution()
print(X.carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))

# Time Complexity : O(NLogN) , where N is number of cars
# Space Complexity : O(N)