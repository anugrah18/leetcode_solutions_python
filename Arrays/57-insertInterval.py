class Solution:
    def insert(self, intervals, newInterval):
        # Initialize the result list to store merged intervals
        res = []

        # Iterate through each interval in the intervals list
        for i in range(len(intervals)):
            # If the new interval comes before the current interval without overlap
            if newInterval[1] < intervals[i][0]:
                # Append the new interval and the remaining intervals to the result list
                res.append(newInterval)
                return res + intervals[i:]
            # If the new interval comes after the current interval without overlap
            elif newInterval[0] > intervals[i][1]:
                # Append the current interval to the result list
                res.append(intervals[i])
            else:
                # Merge the new interval with the current interval by updating the bounds
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # Append the merged new interval to the result list
        res.append(newInterval)
        return res


X = Solution()
print(X.insert([[1,3],[6,9]],[2,5]))

# Time Complexity : O(N)
# Space Complexity : O(1)
