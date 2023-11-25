class Solution(object):
    def intersect(self, nums1, nums2):

        dict = {}
        answer = []
        for num in nums1:
            if (num not in dict):
                dict[num] = 1
            else:
                dict[num] = dict[num] + 1

        for num in nums2:
            if (num in dict and dict[num] > 0):
                dict[num] = dict[num] - 1
                answer.append(num)

        return answer

X = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
answer = X.intersect(nums1,nums2)
print(answer)

# Time Complexity : O(N)
# Space Complexity : O(N)
