class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def dfs(node):
    if not node:
        return

    print(node.val)
    dfs(node.left)
    dfs(node.right)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []  # List to store the serialized tree

        def dfs(node):
            if not node:  # Base case: if the current node is None
                res.append("N")  # Append "N" to represent None
                return
            res.append(str(node.val))  # Append the value of the node as a string
            dfs(node.left)  # Recursively serialize the left subtree
            dfs(node.right)  # Recursively serialize the right subtree

        dfs(root)  # Start the DFS traversal from the root
        return ",".join(res)  # Join the list into a single string

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")  # Split the string into a list of values
        self.i = 0  # Initialize an index to keep track of the current position in the list

        def dfs():
            if vals[self.i] == "N":  # Base case: if the current value is "N"
                self.i += 1  # Move to the next value
                return None  # Return None to represent a null node
            node = TreeNode(int(vals[self.i]))  # Create a new node with the current value
            self.i += 1  # Move to the next value
            node.left = dfs()  # Recursively deserialize the left subtree
            node.right = dfs()  # Recursively deserialize the right subtree
            return node  # Return the node

        return dfs()  # Start the DFS traversal from the first value in the list


root=TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

X = Codec()
Y = X.serialize(root)
Z = X.deserialize(Y)
print(Y)
print(dfs(Z))

# Time Complexity : O(N)
# Space Complexity : O(N)
