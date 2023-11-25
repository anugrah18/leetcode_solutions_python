class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = (360 / 60) * minutes
        h = (360 / 12) * hour + ((minutes / 60) * (360 / 12))

        diff = abs(h - m)

        return min(diff, 360 - diff)


X = Solution()
print(X.angleClock(12,30))