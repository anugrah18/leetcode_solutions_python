class Solution:
    def findOrder(self, numCourses ,prerequisites):
        queue = []
        graph = {}
        indegree = [0] * numCourses
        ans = []

        for i in range(numCourses):
            graph[i] = []

        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            indegree[courses[0]]+=1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.pop(0)
            ans.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return ans if len(ans)==numCourses else []


X = Solution()
print(X.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))

# Time Complexity : O(E+V), V = number of courses , E = number of dependencies
# Space Complexity : O(E+V)


