class Solution(object):
    def merge(self, intervals):
        # Sort the intervals based on the starting times
        intervals.sort(key=lambda x: x[0])

        # Initialize an empty list to store merged intervals
        merged = []

        # Iterate through each interval
        for interval in intervals:
            # If merged is empty or the last interval in merged does not overlap with the current interval
            if len(merged) == 0 or merged[-1][1] < interval[0]:
                # Append the current interval to merged
                merged.append(interval)
            else:
                # There is an overlap, so merge the current interval with the last interval in merged
                merged[-1][1] = max(merged[-1][1], interval[1])

        # Return the list of merged intervals
        return merged


X = Solution()
print(X.merge([[1,5],[2,9],[13,15]]))

# Time complexity : O(nlogn)

# Space complexity : O(n)