class Solution:
    def validTree(self,n,edges):
        if len(edges) != n-1:
            return False

        def createGraph():
            graph={}
            for i in range(n):
                graph[i]=[]
            for edge in edges:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])

            return graph

        def dfs(vertice,parent):
            if vertice in visited:
                return
            visited.add(vertice)
            for neighbor in graph[vertice]:
                if neighbor==parent:
                    continue
                result = dfs(neighbor,vertice)
                if not result:
                    return False
            return True

        graph = createGraph()
        visited=set()
        return dfs(0,-1) and len(visited)==n

X = Solution()
print(X.validTree(5,[[0,1],[0,2],[0,3],[1,4]]))

# Time Complexity : O(N+E) , N = number of nodes , E = number of edges
# Space Complexity : O(N+E)
