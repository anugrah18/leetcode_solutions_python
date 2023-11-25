class Node:
    def __init__(self, content):
        self.content = content
        self.next = {}
        self.isFile = False


class FileSystem:

    def __init__(self):
        self.head = Node('head')

    # Time Complexity : O(M + KlogK) M = longest path , K = number of keys in next of last node
    # Space Complexity: O(M)
    def ls(self, path: str):
        path = path.split('/')

        curr = self.head
        fileName = ''
        for i in path:
            if i != '':
                if i in curr.next:
                    fileName = i
                    curr = curr.next[i]
                else:
                    return []
        if not curr.isFile:
            return sorted(curr.next.keys())
        else:
            return [fileName]

    # Time Complexity : O(M)
    # Space Complexity: O(M)
    def mkdir(self, path: str) -> None:
        curr = self.head
        path = path.split('/')

        for i in path:
            if i != '':
                if i in curr.next:
                    curr = curr.next[i]
                else:
                    curr.next[i] = Node('')
                    curr = curr.next[i]

    # Time Complexity : O(M)
    # Space Complexity: O(M)
    def addContentToFile(self, filePath: str, content: str) -> None:
        filePath = filePath.split('/')
        curr = self.head
        for i in filePath:
            if i != '':
                if i in curr.next:
                    curr = curr.next[i]
                else:
                    curr.next[i] = Node('')
                    curr = curr.next[i]
        curr.content += content
        curr.isFile = True

    # Time Complexity : O(M)
    # Space Complexity: O(M)
    def readContentFromFile(self, filePath: str) -> str:
        filePath = filePath.split('/')
        curr = self.head
        for i in filePath:
            if i != "":
                if i in curr.next:
                    curr = curr.next[i]
                else:
                    return ""
        return curr.content if curr.isFile else ""

X= FileSystem()
print(X.ls("/"))
print(X.mkdir("/a/b/c"))
print(X.addContentToFile("/a/b/c/d","hello"))
print(X.ls("/"))
print(X.readContentFromFile("/a/b/c/d"))
