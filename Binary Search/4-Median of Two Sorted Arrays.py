class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            # First cut on A
            i = (l + r) // 2
            # Second cut on B
            j = half - i - 2

            Aleft = A[i] if i >= 0 else -float('inf')
            Aright = A[i + 1] if (i + 1) < len(A) else float('inf')

            Bleft = B[j] if j >= 0 else -float('inf')
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # for odd number of elements
                if total % 2:
                    return min(Aright, Bright)
                # for even number of elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


X = Solution()
print(X.findMedianSortedArrays([2,3,6,15],[1,3,4,7,10,12]))





