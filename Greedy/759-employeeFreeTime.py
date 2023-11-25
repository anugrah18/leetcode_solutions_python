
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule):
        if not schedule:
            return []

        intervals = []
        ans = []
        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])

        intervals.sort()
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]

            if (currStart > lastEnd):
                ans.append(Interval(lastEnd, currStart))
            lastEnd = max(lastEnd, currEnd)

        return ans

X = Solution()
interval1 = Interval(1,2)
interval2 = Interval(5,6)
interval3 = Interval(1,3)
interval4 = Interval(4,10)
for x in  X.employeeFreeTime([[interval1,interval2],[interval3],[interval4]]):
    print(x.start,x.end)
