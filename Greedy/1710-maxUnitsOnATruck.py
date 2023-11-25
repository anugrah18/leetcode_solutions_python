class Solution:
    def maximumUnits(self, boxTypes, truckSize):

        boxTypes = sorted(boxTypes, key=lambda x: (-x[1]))
        ans = 0

        for box in boxTypes:
            boxCount = min(box[0], truckSize)
            ans += boxCount * box[1]
            truckSize -= boxCount
            if truckSize == 0:
                break

        return ans

X = Solution()
print(X.maximumUnits([[1,3],[2,2],[3,1]],4))

# Time Complexity : O(NlogN)
# Space Complexity : O(1)
