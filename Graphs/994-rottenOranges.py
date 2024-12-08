class Solution(object):
    def orangesRotting(self, grid):
        # Find initial positions of rotten oranges (value 2)
        rotten = self.find_orange(grid, 2)

        # Find initial positions of fresh oranges (value 1)
        fresh = self.find_orange(grid, 1)
        fresh_count = len(fresh)  # Count of fresh oranges

        count = 0  # Time elapsed (in minutes)

        # If no fresh oranges exist, return 0
        if fresh_count <= 0:
            return count

        # Perform BFS until all fresh oranges are rotten or no more can be rotted
        while rotten:
            # Spread infection to adjacent fresh oranges
            rotten = self.spreadInfection(grid, rotten)

            # Reduce fresh orange count by the number of newly rotted oranges
            fresh_count = fresh_count - len(rotten)

            # Increment the time counter
            count = count + 1

            # If no fresh oranges remain, return the time taken
            if fresh_count <= 0:
                return count

        # If there are still fresh oranges left, return -1 (not all oranges can rot)
        return -1

    # Function to spread the infection (rot fresh oranges)
    def spreadInfection(self, grid, rotten=[]):
        new_rotten = []  # List to store newly rotten oranges

        # Process all current rotten oranges
        while len(rotten) > 0:
            (i, j) = rotten.pop(0)  # Get the position of the current rotten orange

            # Check and infect the adjacent oranges (up, down, left, right)
            if (i > 0) and (grid[i - 1][j] == 1):  # Up
                grid[i - 1][j] = 2  # Infect the orange
                new_rotten.append((i - 1, j))  # Add to the new rotten list
            if (i < (len(grid) - 1)) and (grid[i + 1][j] == 1):  # Down
                grid[i + 1][j] = 2
                new_rotten.append((i + 1, j))
            if (j > 0) and (grid[i][j - 1] == 1):  # Left
                grid[i][j - 1] = 2
                new_rotten.append((i, j - 1))
            if (j < (len(grid[0]) - 1)) and (grid[i][j + 1] == 1):  # Right
                grid[i][j + 1] = 2
                new_rotten.append((i, j + 1))

        return new_rotten  # Return all newly rotten oranges

    # Helper function to find all oranges of a given value (1 for fresh, 2 for rotten)
    def find_orange(self, grid, value):
        oranges = []  # List to store positions of oranges with the given value
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == value:  # Check if the cell matches the value
                    oranges.append((i, j))  # Add the position to the list
        return oranges


# Example usage:
X = Solution()
print(X.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # Output: 4

# Time Complexity: O(MN), where M and N are the dimensions of the grid
# - Each cell is processed at most once.

# Space Complexity: O(MN)
# - The space is used to store the positions of rotten and fresh oranges.
