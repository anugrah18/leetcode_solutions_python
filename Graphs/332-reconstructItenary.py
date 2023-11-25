class Solution(object):
    def findItinerary(self, tickets):

        graph = {}
        ans = []

        for ticket in tickets:
            if (ticket[0] not in graph):
                graph[ticket[0]] = []
                graph[ticket[0]].append(ticket[1])
            else:
                graph[ticket[0]].append(ticket[1])

        #For Lexical sorting
        for node in graph:
            graph[node] = sorted(graph[node])

        def dfs(src):
            if (src in graph):
                while (graph[src]):
                    #poping the neighbors from beginning for lexical ordering
                    dfs(graph[src].pop(0))
            ans.append(src)

        dfs('JFK')
        return (ans[::-1])

X = Solution()
print(X.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))