class Solution:
    def wallsAndGates(self, rooms):
        """
        Modify the input grid `rooms` in-place by filling each empty room (INF)
        with the distance to its nearest gate (0).

        -1 = wall
         0 = gate
         INF = empty room (2^31 - 1)
        """
        ROWS, COLS = len(rooms), len(rooms[0])  # Grid dimensions
        visit = set()  # To keep track of visited cells
        q = []  # Queue for BFS traversal

        # Helper to add valid neighboring rooms to the queue
        def addRoom(r, c):
            # If out of bounds, already visited, or it's a wall (-1), skip
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                    (r, c) in visit or rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        # Step 1: Find all gates (cells with value 0) and enqueue them
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0  # Distance from the gate

        # Step 2: BFS from all gates simultaneously
        while q:
            for i in range(len(q)):
                r, c = q.pop(0)  # Dequeue current cell
                rooms[r][c] = dist  # Update the distance in-place
                # Add adjacent cells
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1  # Increment distance for next BFS layer

X = Solution()
rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
X.wallsAndGates(rooms)
print(rooms)

# Time Complexity : O(MN)
# Space Complexity : O(MN), visit may store every cell

