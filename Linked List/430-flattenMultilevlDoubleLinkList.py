class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):

        if not head:
            return None

        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while (stack):
            curr = stack.pop()
            prev.next = curr
            curr.prev = prev

            if (curr.next):
                stack.append(curr.next)

            if (curr.child):
                stack.append(curr.child)
                curr.child = None
            prev = curr

        pseudoHead.next.prev = None
        return pseudoHead.next
"""
Input:

1<->2<->4
    |
    3<->5<->6
        |
        7
"""
node1 = Node(1,None,None,None)
node2 = Node(2,None,None,None)
node3 = Node(3,None,None,None)
node4 = Node(4,None,None,None)
node5 = Node(5,None,None,None)
node6 = Node(6,None,None,None)
node7 = Node(7,None,None,None)
node1.next = node2
node2.prev = node1
node2.next = node4
node4.prev = node2
node2.child = node3
node3.next = node5
node5.prev = node3
node5.child = node7
node5.next = node6
node6.prev = node5

X = Solution()
res = X.flatten(node1)

while(res):
    print(res.val)
    res= res.next


# Time Complexity: O(N)
# Space Complexity : O(N)


