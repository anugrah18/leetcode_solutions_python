class Node:
    def __init__(self, val=None, next=None):
        self.data = val
        self.next = next


class LinkedList:
    length = 0
    head = Node()

    def __init__(self, val=None, next=None):
        self.head.data = val
        self.head.next = next

    def append(self, val):
        if (self.head.data == None):
            self.head.data = val
            self.head.next = None
            self.length = self.length + 1
            return

        ptr = self.head
        while (ptr.next != None):
            ptr = ptr.next

        newNode = Node(val)
        newNode.next = None
        ptr.next = newNode
        self.length = self.length + 1

    def print(self):
        ptr = self.head
        while (ptr != None):
            print(ptr.data)
            ptr = ptr.next

    def prepend(self, val):
        if (self.head.data == None):
            newNode = Node(val)
            newNode.next = None
            self.length = self.length + 1
            return

        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.length = self.length + 1

    def getLength(self):
        return self.length

    def delete(self,index):
        if(index >= self.length):
            print("Out of index")
            return
        if (index == 0):
            self.head= self.head.next
            self.length= self.length-1
            return

        prevPtr = self.head
        curPtr = prevPtr.next

        for i in range (1,self.length):
            if(index == i):
                prevPtr.next = curPtr.next
                return
            prevPtr = prevPtr.next
            curPtr = curPtr.next

linkList = LinkedList()
linkList.append(1)
linkList.append(2)
linkList.append(3)
linkList.prepend(0)
linkList.prepend(-2)
linkList.delete(4)

linkList.print()

#print(linkList.getLength())




