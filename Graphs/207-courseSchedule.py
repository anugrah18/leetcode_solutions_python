class Solution(object):
    def canFinish(self, numCourses, prerequisites):

        graph = {}
        queue = []
        indegree = [0] * numCourses
        count = 0

        # initialize graph with all courses as vertices
        for i in range(numCourses):
            graph[i] = []

        # create adjacency list and indegree
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            indegree[courses[0]] += 1

        # append in queue all vertices with zero indegree
        for i in range(len(indegree)):
            if (indegree[i] == 0):
                queue.append(i)

        # find cycle in graph
        while (queue):
            curr = queue.pop(0)
            count += 1
            neighbors = graph[curr]
            for neighbor in neighbors:
                indegree[neighbor] = indegree[neighbor] - 1
                if (indegree[neighbor] == 0):
                    queue.append(neighbor)

        if (count == numCourses):
            return True
        else:
            return False

X =Solution()
print(X.canFinish(4,[[1,0],[2,1],[3,2]]))

# Time Complexity : O(E+V), V = number of courses , E = number of dependencies
# Space Complexity : O(E+V)