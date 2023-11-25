class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        cur = self
        while(cur!=None):
            print(cur.val)
            cur= cur.next


class Solution(object):


    def addTwoNumbers(self, l1, l2):

        ans = ListNode(0)
        ans_tail = ans
        carry = 0

        while(l1 or l2):
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            out = (val1+val2+carry)%10
            carry = int((val1+val2+carry)/10)

            ans_tail.next = ListNode(out)
            ans_tail = ans_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        if (carry > 0):
            ans_tail.next = ListNode(carry)
            ans_tail = ans_tail.next

        return ans.next


list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(9)

list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)

X = Solution()
res = X.addTwoNumbers(list1,list2)

res.printList()

# Time Complexity : O(N) , N = max length of two lists
# Space Complexity : O(N) , N = max length of two lists
