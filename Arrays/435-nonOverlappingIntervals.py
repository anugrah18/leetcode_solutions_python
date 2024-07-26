class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Sort the intervals based on their starting times
        intervals = sorted(intervals, key=lambda x: x[0])

        # Initialize the result counter for the number of intervals to remove
        res = 0
        # Initialize prevEnd to the end of the first interval
        prevEnd = intervals[0][1]

        # Iterate through the intervals starting from the second interval
        for start, end in intervals[1:]:
            # If there is no overlap, update prevEnd to the current end
            if start >= prevEnd:
                prevEnd = end
            else:
                # If there is an overlap, increment the result counter
                res += 1
                # Update prevEnd to the minimum end time to maximize the non-overlapping space
                prevEnd = min(end, prevEnd)

        # Return the number of intervals to remove to make the rest non-overlapping
        return res


X = Solution()
print(X.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

# Time Complexity = O(NlogN)
# Space Complexity = O(N)

