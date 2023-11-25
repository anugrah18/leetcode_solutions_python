class Solution:
    def minMeetingRooms(self, intervals) -> int:
        res, rooms = 0, 0
        startTimings, endTimings = [], []

        e = 0
        s = 0

        for i in range(len(intervals)):
            startTimings.append(intervals[i][0])
            endTimings.append(intervals[i][1])

        startTimings.sort()
        endTimings.sort()

        while s < len(intervals):
            if startTimings[s] < endTimings[e]:
                s += 1
                rooms += 1
            else:
                e += 1
                rooms -= 1
            res = max(rooms, res)

        return res


X = Solution()
print(X.minMeetingRooms([[0,30],[5,10],[15,20]]))

# Time Complexity : O(NLogN)
# Space Complexity : O(N)
