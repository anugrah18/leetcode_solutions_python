class Solution:
    def alienOrder(self, words):
        """
        This function determines the order of characters in an alien language given a sorted list of words.
        :param words: List of words sorted in alien dictionary order.
        :return: A string representing the order of characters, or an empty string if it's not possible.
        """

        # Step 1: Initialize the adjacency list for the graph
        adj = {}  # Adjacency list to represent character dependencies
        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = set()  # Each character points to a set of characters that come after it

        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # If the prefix of the first word is longer than the second word, it's invalid
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Compare characters of the two words and determine the order
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])  # w1[j] must come before w2[j]
                    break  # Stop comparing once the first differing character is found

        # Step 3: Perform a topological sort using DFS
        visit = {}  # Dictionary to track the visitation state of nodes (False = visited, True = visiting)
        res = []  # List to store the topological order

        def dfs(c):
            """
            Perform a depth-first search to detect cycles and build the topological order.
            :param c: The current character being visited.
            :return: True if a cycle is detected, False otherwise.
            """
            if c in visit:
                return visit[c]  # If visiting (True), a cycle is detected; if visited (False), skip
            visit[c] = True  # Mark as visiting
            for neighbor in adj[c]:
                if dfs(neighbor):  # Recursive DFS call for neighbors
                    return True  # Cycle detected
            visit[c] = False  # Mark as visited
            res.append(c)  # Add the character to the result
            return False

        # Step 4: Visit all characters in the graph
        for c in adj:
            if dfs(c):  # If a cycle is detected, return an empty string
                return ""

        # Step 5: Reverse the result to get the correct topological order
        res = res[::-1]
        return "".join(res)  # Return the result as a string


# Example usage:
X = Solution()
print(X.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))  # Output: "wertf"

# Time Complexity: O(C), where C is the total number of characters in all the words combined
# - Initializing the adjacency list takes O(C).
# - Building the graph involves comparing adjacent words, taking O(C).
# - DFS traversal takes O(C) since each character and edge is visited once.

# Space Complexity: O(V + E) for the graph and recursion stack
# - V = unique characters (number of nodes in the graph).
# - E = number of edges (dependencies between characters).
