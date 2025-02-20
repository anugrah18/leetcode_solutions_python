class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []  # Stack to store valid directory names
        curr = ""  # Temporary variable to hold directory names

        # Append "/" at the end to ensure the last component is processed
        for c in path + "/":
            if c == "/":  # Encountering a slash means end of a directory name
                if curr == "..":
                    if stack:  # If stack is not empty, go up one level
                        stack.pop()
                elif curr and curr != ".":  # Ignore empty components and "."
                    stack.append(curr)  # Push valid directory name
                curr = ""  # Reset current component after processing
            else:
                curr += c  # Build the current directory name

        return "/" + "/".join(stack)  # Join stack to form the final simplified path


X = Solution()
print(X.simplifyPath("/home/user/Documents/../Pictures"))

# Time Complexity : O(N) , N is the number of characters in the string.
# Space Complexity : O(N)
