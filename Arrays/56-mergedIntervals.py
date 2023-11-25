
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if (len(merged) == 0 or merged[-1][1] < interval[0]):
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

X = Solution()
print(X.merge([[1,5],[2,9],[13,15]]))

# Time complexity : O(nlogn)

# Space complexity : O(n)