class Node:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self,val=None):
        self.root = Node()

    def insertNode(self,data):
        if(self.root.val == None):
            self.root.val=data
            return
        else:
            ptr = self.root
            while(ptr):
                if(data <= ptr.val):
                    if(ptr.left == None):
                        ptr.left = Node(data)
                        return
                    else:
                        ptr = ptr.left
                else:
                    if(data> ptr.val):
                        if(ptr.right == None):
                            ptr.right = Node(data)
                            return
                        else:
                            ptr=ptr.right

    def preOrderTraversal(self,node):
        if(node):
            print(node.val)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def inOrderTraversal(self,node):
        if(node):
            self.inOrderTraversal(node.left)
            print(node.val)
            self.inOrderTraversal(node.right)

    def postOrderTraversal(self,node):
        if(node):
            self.postOrderTraversal(node.left)
            self.postOrderTraversal(node.right)
            print(node.val)

BST = BinarySearchTree()
BST.insertNode(5)
BST.insertNode(1)
BST.insertNode(9)
BST.insertNode(3)
BST.insertNode(6)
#BST.preOrderTraversal(BST.root)
BST.inOrderTraversal(BST.root)
#BST.postOrderTraversal(BST.root)
