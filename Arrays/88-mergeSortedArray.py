class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # p1 is the pointer for nums1 (starting from the end of the valid part)
        p1 = m - 1
        # p2 is the pointer for nums2 (starting from the end)
        p2 = n - 1
        # p is the pointer for the merged array (starting from the end)
        p = m + n - 1

        # Iterate while both p1 and p2 are within bounds
        while p1 >= 0 and p2 >= 0:
            # Compare elements from the end of nums1 and nums2
            if nums1[p1] <= nums2[p2]:
                # If nums2[p2] is greater or equal, place it at the current position of p in nums1
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                # If nums1[p1] is greater, place it at the current position of p in nums1
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them over to nums1
        nums1[:p2 + 1] = nums2[:p2 + 1]



# Time Complexity : O(n+m)
# Space Complexity : O(1)