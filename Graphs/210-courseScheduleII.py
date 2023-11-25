class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        queue = []
        graph = {}
        indegree = [0] * numCourses
        count = 0
        res = []

        for i in range(numCourses):
            graph[i] = []

        for course in prerequisites:
            graph[course[1]].append(course[0])
            indegree[course[0]] += 1

        for i in range(len(indegree)):
            if (indegree[i] == 0):
                queue.append(i)
                res.append(i)

        while (queue):
            curr = queue.pop(0)
            neighbors = graph[curr]
            count += 1

            for neighbor in neighbors:
                indegree[neighbor] -= 1
                if (indegree[neighbor] == 0):
                    queue.append(neighbor)
                    res.append(neighbor)

        if (count == numCourses):
            return res
        else:
            return []


X = Solution()
print(X.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))

# Time Complexity : O(E+V), V = number of courses , E = number of dependencies
# Space Complexity : O(E+V)


