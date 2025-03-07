"""
For M, N  generate all paths from top left to bottom right assuming you can only move in two directions
Down and Right
"""


def find_paths_with_grid(m, n, path="", grid_path=None, i=0, j=0, result=None):
    if result is None:
        result = []
    # grid_path is optional
    if grid_path is None:
        grid_path = []
    # grid_path is optional
    grid_path.append((i, j))  # Add current position to path

    if i == m - 1 and j == n - 1:
        # grid_path is optional
        result.append((path, grid_path[:]))  # Store both path and grid numbers
        return result

    if i < m - 1:
        # grid_path is optional
        find_paths_with_grid(m, n, path + "D", grid_path[:], i + 1, j, result)

    if j < n - 1:
        # grid_path is optional
        find_paths_with_grid(m, n, path + "R", grid_path[:], i, j + 1, result)

    return result


# Example usage
M, N = 2, 3  # Example for a 2x3 grid
paths = find_paths_with_grid(M, N)

# Print paths with grid positions
for p, grid in paths:
    print(f'Path: "{p}", Grid Path: {grid}')

# Time Complexity : O(2^(m+n-2))
# Space Complexity : O(2^(m+n-2))
