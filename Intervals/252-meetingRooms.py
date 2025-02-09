class Solution:
    def canAttendMeetings(self, intervals):
        # Sort the intervals based on their starting times
        intervals = sorted(intervals, key=lambda x: x[0])

        # Iterate through the intervals starting from the second interval
        for i in range(1, len(intervals)):
            # If the end time of the previous interval is greater than the start time of the current interval
            if intervals[i - 1][1] > intervals[i][0]:
                # Return False since the meetings overlap
                return False

        # Return True if no overlapping intervals are found
        return True


X =Solution()
print(X.canAttendMeetings([[0,30],[5,10],[15,20]]))

# Time Complexity : O(NlogN)
# Space Complexity : O(1)