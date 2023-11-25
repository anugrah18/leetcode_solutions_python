import timeit

class Solution(object):
    def __init__(self):
        self.graph = {}
        self.queue =[]

    def insertNode(self,node):
        if(node not in self.graph):
            self.graph[node] =[]
        else:
            print(node + " already exist!")

    def insertEdge(self,node1,node2):
        if(node1 in self.graph and node2 in self.graph):
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        else:
            print("Both nodes should exist in graph")

    def printGraph(self):
        print(self.graph)

    #DFS Using Recursion
    def DFS(self,node,visited=[]):
        if node not in visited:
            print(node, end= " ")
            visited.append(node)
            for neighbour in self.graph[node]:
                self.DFS(neighbour,visited)

    #BFS Using Recursion
    def BFS(self,node,visited=[]):
        self.queue.append(node)
        visited.append(node)
        while(self.queue):
            s = self.queue.pop(0)
            print(s , end= " ")
            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    self.queue.append(neighbour)


    def DFSTraversal(self,node):
        if(node not in self.graph):
            print(node + " does not exist in graph!")
            return
        stack = []
        visited = []
        stack.append(node)
        visited.append(node)
        print(node)

        while(stack):
            #check if all adjacent nodes for node on top of stack is visited
            intersect = list(set(self.graph[stack[-1]]) & set(visited))
            if (set(intersect) == set(self.graph[stack[-1]])):
                stack.pop()
            #add unvisited nodes to stack,visited and print the node
            else:
                adjNodes = self.graph[stack[-1]]
                for node in adjNodes:
                    if(node not in visited):
                        stack.append(node)
                        visited.append(node)
                        print(node)
                        break


    def BFSTraversal(self,node):
        if (node not in self.graph):
            print(node + " does not exist in graph!")
            return
        queue = []
        visited = []
        queue.append(node)
        visited.append(node)

        while(queue):
            #To check if front node in queue has all visited adjacent nodes
            interesect = list(set(visited) & set(self.graph[queue[0]]))
            if(set(interesect) == set(self.graph[queue[0]])):
                print(queue.pop(0))
            #append adjacent nodes to queue
            else:
                adjNode = self.graph[queue[0]]
                for node in adjNode:
                    if(node not in visited):
                        queue.append(node)
                        visited.append(node)
                        
X = Solution()
X.insertNode("1")
X.insertNode("2")
X.insertNode("3")
X.insertNode("4")
X.insertNode("5")
X.insertNode("6")
X.insertNode("7")

X.insertEdge("1","2")
X.insertEdge("1","3")
X.insertEdge("1","7")
X.insertEdge("2","3")
X.insertEdge("1","4")
X.insertEdge("3","5")
X.insertEdge("4","5")
X.insertEdge("5","6")


X.BFS("1")
print()
X.DFS("1")









