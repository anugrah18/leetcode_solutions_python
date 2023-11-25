class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i - 1][1] > intervals[i][0]:
                return False

        return True

X =Solution()
print(X.canAttendMeetings([[0,30],[5,10],[15,20]]))

# Time Complexity : O(NlogN)
# Space Complexity : O(1)