class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def VerticalTraversal(self,root):
        node_list = []

        def DFS(column,row,node):
            if(node != None):
                node_list.append((column,row,node.val))
                DFS(column-1,row+1,node.left)
                DFS(column+1,row+1,node.right)

        DFS(0,0,root)
        node_list.sort()

        curr_column_index = node_list[0][0]
        curr_column = []
        ans = []

        for column,row,value in node_list:
            if (column == curr_column_index):
                curr_column.append(value)
            else:
                ans.append(curr_column)
                curr_column_index=column
                curr_column=[value]

        ans.append(curr_column)

        return ans

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

X = Solution()
print(X.VerticalTraversal(root))




