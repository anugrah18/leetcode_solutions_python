class Solution:
    def isNStraightHand(self, hand, groupSize):
        n = len(hand)
        if n % groupSize != 0:
            return False

        hand.sort()

        # Build frequency dictionary manually
        freq = {}
        for num in hand:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for num in hand:
            # If this number has already been used, skip it
            if freq[num] == 0:
                continue

            # Try to build a group starting from num
            for i in range(groupSize):
                next_num = num + i
                if next_num not in freq or freq[next_num] == 0:
                    return False
                freq[next_num] -= 1

        return True

# Time Complexity : O(NLogN) , N = hands
# Space Complexity : O(N)