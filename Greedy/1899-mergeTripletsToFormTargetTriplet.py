class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        # Set to keep track of indices where target values are matched
        good = set()
        # Iterate through each triplet
        for t in triplets:
            # Skip triplet if any element is greater than the corresponding element in target
            # Because we cannot use such a triplet to build the target (we can only increase values)
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                # If the value at index i matches target[i], record that this component is satisfied
                if v == target[i]:
                    good.add(i)
        # We can form the target only if we matched all three indices
        return len(good) == 3


X = Solution()
print(X.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]],[2,7,5]))

# Time Complexity : O(N)
# Space Complexity : O(1)