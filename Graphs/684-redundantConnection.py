class Solution:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        # Add the edge to the graph in both directions (undirected)
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def hasPath(self, start, end, visited):
        # DFS to check if a path exists from start to end
        if start == end:
            return True
        visited.add(start)

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                if self.hasPath(neighbor, end, visited):
                    return True
        return False

    def findRedundantConnection(self, edges):
        for u, v in edges:
            visited = set()

            # Check if adding this edge would form a cycle
            if u in self.graph and v in self.graph and self.hasPath(u, v, visited):
                return [u, v]

            # Otherwise, add the edge to the graph
            self.addEdge(u, v)



X = Solution()
print(X.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))

# Time Complexity : O(N^2)
# Space Complexity : O(N)
