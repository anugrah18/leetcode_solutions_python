class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    visited = {}
    def cloneGraph(self,node):
        if not node:
            return
        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val,[])
        self.visited[node]=clone_node

        if node.neighbors:
            for neighbor in node.neighbors:
                clone_node.neighbors.append(self.cloneGraph(neighbor))

        return clone_node

    def dfs(self,node,visit=[]):
        visit.append(node.val)
        print(node.val)
        for neighbor in node.neighbors:
            if neighbor.val not in visit:
                self.dfs(neighbor,visit)

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


