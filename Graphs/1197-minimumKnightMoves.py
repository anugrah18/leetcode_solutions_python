class Solution:
    def minKnightMoves(self, x, y) -> int:
        steps = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        visited = set()

        queue = [(0, (0, 0))]

        while (queue):
            moves, coord = queue.pop(0)
            if coord[0] == x and coord[1] == y:
                return moves

            for s in steps:
                next_step = (coord[0] + s[0], coord[1] + s[1])

                # restrict traversal in one quadrant
                if not ((next_step[0] >= -2 and x >= -2 and next_step[1] >= -2 and y >= -2) or
                        (next_step[0] <= 2 and x <= 2 and next_step[1] <= 2 and y <= 2) or
                        (next_step[0] >= -2 and x >= -2 and next_step[1] <= 2 and y <= 2) or
                        (next_step[0] <= 2 and x <= 2 and next_step[1] >= -2 and y >= -2)):
                    continue

                if next_step not in visited:
                    queue.append((moves + 1, next_step))
                    visited.add(next_step)


X = Solution()
print(X.minKnightMoves(5,5))

# Time Complexity : O(max(x,y)^2) , since we are restricting into one quadrant maximum square of either x,y as side
# Space Complexity : O(max(x,y)^2)

