class Solution:
    def validTree(self, n, edges):
        # A valid tree must have exactly n-1 edges (if not, it can't be a tree)
        if len(edges) != n - 1:
            return False

        # Function to create an adjacency list representation of the graph
        def createGraph():
            graph = {}
            # Initialize the adjacency list with empty lists for each node
            for i in range(n):
                graph[i] = []
            # Populate the adjacency list with the edges
            for edge in edges:
                graph[edge[0]].append(edge[1])  # Add edge from node A to B
                graph[edge[1]].append(edge[0])  # Add edge from node B to A (undirected graph)
            return graph

        # Depth-First Search (DFS) function to check for cycles and connectivity
        def dfs(vertice, parent):
            # If the current node is already visited, there's a cycle
            if vertice in visited:
                return
            # Mark the current node as visited
            visited.add(vertice)
            # Traverse all neighbors of the current node
            for neighbor in graph[vertice]:
                if neighbor == parent:
                    # Skip the parent node to avoid counting it as a cycle
                    continue
                # Recursively call DFS for the neighbor
                result = dfs(neighbor, vertice)
                if not result:  # If a cycle is detected in the recursion, return False
                    return False
            return True  # Return True if no cycles are detected

        # Create the graph from the edges
        graph = createGraph()
        visited = set()  # Initialize a set to track visited nodes

        # Perform DFS starting from node 0 and check two conditions:
        # 1. DFS must return True (no cycles detected).
        # 2. All nodes must be visited (graph is connected).
        return dfs(0, -1) and len(visited) == n


# Example usage:
X = Solution()
print(X.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # Output: True

# Time Complexity: O(N + E)
# - N = number of nodes, E = number of edges.
# - Constructing the graph takes O(N + E).
# - DFS traverses all nodes and edges, also O(N + E).

# Space Complexity: O(N + E)
# - Space for the adjacency list representation of the graph (O(N + E)).
# - Space for the visited set (O(N)).
