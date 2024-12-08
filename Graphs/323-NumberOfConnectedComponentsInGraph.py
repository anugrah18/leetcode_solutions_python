class Solution:
    def __init__(self):
        # Initialize an empty graph represented as an adjacency list
        self.graph = {}

    def ConstructGraph(self, edges):
        # Build the graph from the given edges
        for edge in edges:
            start, end = edge  # Each edge connects two nodes: start and end

            # Add the edge to the adjacency list for both nodes (undirected graph)
            if start not in self.graph:
                self.graph[start] = []
            self.graph[start].append(end)

            if end not in self.graph:
                self.graph[end] = []
            self.graph[end].append(start)

    def dfs(self, node, visited):
        # Perform depth-first search (DFS) to explore all connected nodes
        if node not in self.graph:
            return  # If the node is not in the graph, return

        for neighbor in self.graph[node]:  # Iterate over all neighbors of the node
            if not visited[neighbor]:  # If the neighbor is not visited
                visited[neighbor] = True  # Mark the neighbor as visited
                self.dfs(neighbor, visited)  # Recursively perform DFS for the neighbor

    def CountComponents(self, n, edges):
        # Count the number of connected components in the graph
        if not edges:
            return n  # If there are no edges, each node is its own component

        connectedComponents = 0  # Initialize the count of connected components
        self.ConstructGraph(edges)  # Construct the graph from the edges
        visited = [False] * n  # Keep track of visited nodes

        for node in range(n):  # Iterate through all nodes
            if not visited[node]:  # If the node is not visited
                connectedComponents += 1  # Increment the count of connected components
                visited[node] = True  # Mark the node as visited
                self.dfs(node, visited)  # Perform DFS to explore all connected nodes

        return connectedComponents  # Return the total number of connected components

# Example usage:
X = Solution()
print(X.CountComponents(5, [[0, 1], [1, 2], [3, 4]]))  # Output: 2

# Explanation:
# The graph has 5 nodes (0 to 4) and 2 connected components:
# - Component 1: [0, 1, 2]
# - Component 2: [3, 4]

# Time Complexity: O(N + E)
# - N is the number of nodes, and E is the number of edges.
# - Constructing the graph and performing DFS for all nodes takes O(N + E).

# Space Complexity: O(N + E)
# - Space is used for the adjacency list representation of the graph and the visited list.
