class Solution:
    def shortestPathBinaryMatrix(self, grid):
        N = len(grid)  # Size of the NxN grid

        # Initialize BFS queue with starting position (row=0, col=0) and path length 1
        q = []
        q.append((0, 0, 1))

        # to track visited cells
        visit = set((0, 0))

        # 8 possible directions (horizontal, vertical, diagonal)
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        while q:
            # Get current position and path length from queue
            r, c, l = q.pop(0)

            # Skip if out of bounds or on a blocked cell
            if min(r, c) < 0 or max(r, c) >= N or grid[r][c] == 1:
                continue

            # If destination is reached, return the path length
            if r == N - 1 and c == N - 1:
                return l

            # Explore all 8 directions
            for dr, dc in direct:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visit:
                    q.append((nr, nc, l + 1))
                    visit.add((nr, nc))  # Mark as visited

        # No path found
        return -1

X = Solution()
print(X.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))

# Time complexity : O(N^2)
# Space complexity : O(N^2)