import heapq


# Prim's MST algorithm
class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)  # Total number of points
        total_cost = 0  # Result: Total minimum cost to connect all points
        seen = set()  # Keeps track of points already included in MST
        min_heap = [(0, 0)]  # Min-heap of (cost, point_index), starting with cost 0 at point 0

        while len(seen) < n:
            dist, i = heapq.heappop(min_heap)  # Get the point with the smallest cost to connect
            if i in seen:
                continue  # Skip if already in MST
            seen.add(i)  # Mark point as connected
            total_cost += dist  # Add connection cost to total

            xi, yi = points[i]  # Coordinates of the newly added point
            # Check all unvisited points and calculate their distance from point i
            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    # Use Manhattan distance as the cost to connect point i and point j
                    neighbor_dist = abs(xi - xj) + abs(yi - yj)
                    heapq.heappush(min_heap, (neighbor_dist, j))  # Push potential connection to heap

        return total_cost  # Return the total cost of connecting all points with minimum effort


X = Solution()
print(X.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))

# Time Complexity : O(N^2 * LogN) , where N is number of points
# Space Complexity : O(N^2) , min heap can grow to to n^2 entries at a time in worst case
