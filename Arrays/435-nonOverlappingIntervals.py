class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        return res

X = Solution()
print(X.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

# Time Complexity = O(NlogN)
# Space Complexity = O(1)

