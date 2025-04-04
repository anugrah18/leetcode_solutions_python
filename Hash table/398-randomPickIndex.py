import random

# Hash map approach
# Time Complexity : O(N)
# Space complexity : O(N)
class SolutionI:

    def __init__(self, nums):
        self.index_map = {}  # Dictionary to store target -> list of indices

        for i, num in enumerate(nums):
            # If the number is not yet in the map, initialize with an empty list
            if num not in self.index_map:
                self.index_map[num] = []
            # Append the current index to the list of indices for this number
            self.index_map[num].append(i)

    def pick(self, target: int) -> int:
        # Randomly pick one index from the list of indices for the target number
        return random.choice(self.index_map[target])

# Reservoir Sampling approach
# Time Complexity : O(N)
# Space complexity : O(1)
class SolutionII:

    def __init__(self, nums):
        # Store the input list for future pick operations
        self.nums = nums

    def pick(self, target: int) -> int:
        # Counts how many times we've seen the target so far
        count = 0
        # Stores the currently selected index for the target
        picked_index = 0

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1  # Found an occurrence of the target

                # Reservoir Sampling: With probability 1/count, pick this index
                # Ensures each occurrence has equal probability of being picked
                if random.randint(1, count) == count:
                    picked_index = i  # Replace the previously picked index

        return picked_index


X = SolutionI([1,2,3,3,3])
print(X.pick(3))
print(X.pick(1))
print(X.pick(3))

