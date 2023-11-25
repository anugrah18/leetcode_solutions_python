class Solution:
    def __init__(self):
        self.graph = {}

    def ConstructGraph(self,edges):
        for edge in edges:
            start,end = edge

            if start not in self.graph:
                self.graph[start] = []
            self.graph[start].append(end)

            if end not in self.graph:
                self.graph[end] = []
            self.graph[end].append(start)

    def dfs(self,node,visited):
        if node not in self.graph:
            return
        for neighbor in self.graph[node]:
            if visited[neighbor]==False:
                visited[neighbor]=True
                self.dfs(neighbor,visited)

    def CountComponents(self,n,edges):
        if(not edges):
            return n

        connectedComponents = 0
        self.ConstructGraph(edges)
        visited = [False] * n

        for node in range(n):
            if not visited[node]:
                connectedComponents+=1
                visited[node]=True
                self.dfs(node,visited)

        return connectedComponents

X = Solution()
print(X.CountComponents(5,[[0,1],[1,2],[3,4]]))


