import heapq

# Implements Djikstra's shortest distance path
class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        edges = {}  # Adjacency list to represent the graph

        # Build the graph: edges[u] contains list of (v, w) meaning an edge from u to v with weight w
        for u, v, w in times:
            if u not in edges:
                edges[u] = []
            edges[u].append((v, w))

        minHeap = [(0, k)]  # Min-heap to get the next node with the smallest cumulative weight (time)
        visit = set()  # Set to track visited nodes
        t = 0  # Tracks the maximum time taken to reach any node

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)  # Get node with smallest time to reach
            if n1 in visit:
                continue  # Skip if already visited
            visit.add(n1)
            t = max(t, w1)  # Update total time with the longest time so far

            # Explore neighbors of the current node
            if n1 in edges:
                for n2, w2 in edges[n1]:
                    if n2 not in visit:
                        heapq.heappush(minHeap, (w1 + w2, n2))  # Push cumulative time to reach neighbor

        # If all nodes were reached, return total time; otherwise, return -1
        return t if len(visit) == n else -1


X = Solution()
print(X.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))

# Time Complexity : O(E * LogV)
# Space Complexity : O(E + V)
