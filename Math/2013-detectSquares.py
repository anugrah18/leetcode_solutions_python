from collections import defaultdict
from typing import List

class DetectSquares:

    def __init__(self):
        # Dictionary to count occurrences of each point
        # Key = (x, y), Value = count
        self.ptsCount = defaultdict(int)

        # List to store all added points for iteration during counting
        self.pts = []

    def add(self, point: List[int]) -> None:
        # Convert point to tuple (so it can be used as a dict key)
        self.ptsCount[tuple(point)] += 1

        # Add the point to the list of seen points
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point  # Coordinates of the query point

        # Iterate over all previously added points
        for x, y in self.pts:
            # To form a valid square:
            # - Distance between x and px must equal distance between y and py
            # - x and px must not be the same (to avoid vertical line)
            # - y and py must not be the same (to avoid horizontal line)
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue

            # Check if the other two required corners exist
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res

X = DetectSquares()
X.add([3, 10])
X.add([11, 2])
X.add([3, 2])
print(X.count([11, 10]))
print(X.count([14, 8]))
X.add([11, 2])
print(X.count([11, 10]))

# Time Complexity for add() -> O(1) , count() -> O(n)
# Space Complexity for add() -> O(n) , count() -> O(1)