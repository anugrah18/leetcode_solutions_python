class Solution:
    def replaceElements(self, arr):
        ans = [0] * (len(arr))
        max_el = -float('inf')
        for i in range(len(arr) - 1, 0, -1):
            max_el = max(max_el, arr[i])
            ans[i - 1] = max_el

        ans[-1] = -1
        return ans

X = Solution()

print(X.replaceElements([17,18,5,4,6,1]))

# Time Complexity : O(N)
# Space Complexity : O(1)