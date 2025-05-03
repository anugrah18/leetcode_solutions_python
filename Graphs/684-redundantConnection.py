class Solution:
    def findRedundantConnection(self, edges):
        # Helper function to check if there is a path from 'start' to 'end' using DFS
        def has_path(graph, start, end, visited):
            if start == end:
                return True
            visited.add(start)
            if start in graph:
                for neighbor in graph[start]:
                    if neighbor not in visited:
                        if has_path(graph, neighbor, end, visited):
                            return True
            return False

        # Initialize an empty graph using a dictionary
        graph = {}

        # Iterate through each edge
        for u, v in edges:
            visited = set()

            # If both nodes already exist in the graph and there is a path between them,
            # then adding this edge would form a cycle — it's redundant
            if u in graph and v in graph and has_path(graph, u, v, visited):
                return [u, v]

            # Add the edge to the graph (bidirectional since the graph is undirected)
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)


X = Solution()
print(X.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))

# Time Complexity : O(N^2)
# Space Complexity : O(N)
