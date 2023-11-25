class Solution:
    def allPathsSourceToTarget(self,graph):

        target = len(graph)-1

        def allPathToTarget(currNode):
            if(currNode==target):
                return [[target]]

            result = []
            for nextNode in graph[currNode]:
                for path in allPathToTarget(nextNode):
                    result.append([currNode] + path)

            return result

        return allPathToTarget(0)

X = Solution()
print(X.allPathsSourceToTarget([[1,2],[3],[3],[]]))