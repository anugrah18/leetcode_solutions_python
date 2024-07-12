class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    visited = {}  # A class-level dictionary to keep track of visited nodes

    def cloneGraph(self, node):
        # If the input node is None, return None
        if not node:
            return

        # If the node is already visited, return its clone from the visited dictionary
        if node in self.visited:
            return self.visited[node]

        # Create a clone of the current node
        clone_node = Node(node.val, [])
        # Add the clone to the visited dictionary
        self.visited[node] = clone_node

        # Iterate through the neighbors of the node and recursively clone them
        if node.neighbors:
            for neighbor in node.neighbors:
                clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node

    def dfs(self, node, visit=[]):
        # Append the current node's value to the visit list
        visit.append(node.val)
        # Print the current node's value
        print(node.val)
        # Recursively perform DFS on unvisited neighbors
        for neighbor in node.neighbors:
            if neighbor.val not in visit:
                self.dfs(neighbor, visit)

X = Solution()
node1 = Node(1,[])
node2 = Node(2,[])
node3 = Node(3,[])
node4 = Node(4,[])
node1.neighbors = [node2,node4]
node2.neighbors = [node1,node3]
node3.neighbors = [node2,node4]
node4.neighbors = [node1,node3]
node_copy = X.cloneGraph(node1)

X.dfs(node_copy)

# Time Complexity : O(N+M) , N = number of nodes , M = number of edges
# Space Complexity : O(N)


