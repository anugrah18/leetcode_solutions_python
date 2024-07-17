class Solution:
    def minMeetingRooms(self, intervals) -> int:
        res, rooms = 0, 0
        startTimings, endTimings = [], []

        e = 0
        s = 0

        # Separate start and end times from intervals
        for i in range(len(intervals)):
            startTimings.append(intervals[i][0])
            endTimings.append(intervals[i][1])

        # Sort start and end times
        startTimings.sort()
        endTimings.sort()

        # Use two pointers to compare start and end times
        while s < len(intervals):
            if startTimings[s] < endTimings[e]:
                # If a meeting starts before the earliest ending meeting ends, we need a new room
                s += 1
                rooms += 1
            else:
                # If a meeting starts after the earliest ending meeting ends, we can reuse a room
                e += 1
                rooms -= 1
            # Update the maximum number of rooms needed
            res = max(rooms, res)

        return res



X = Solution()
print(X.minMeetingRooms([[0,30],[5,10],[15,20]]))

# Time Complexity : O(NLogN)
# Space Complexity : O(N)
