class Solution:
    def nextGreaterElement(self, nums1, nums2):
        nums1_ht = {}
        for i in range(len(nums1)):
            nums1_ht[nums1[i]] = i

        res = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1_ht[val]
                res[idx] = curr
            if curr in nums1_ht:
                stack.append(curr)

        return res


X = Solution()
print(X.nextGreaterElement([4,1,2],[1,3,4,2]))

# Time Complexity : O(M + N) , M = size of smaller array
# Space Complexity : O(M)