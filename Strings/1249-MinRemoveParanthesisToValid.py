class Solution:
    # Approach 1: Using two-pass string builder.
    # Time Complexity = O(N)
    # Space Complexity = O(N)
    def minRemoveToMakeValid_1(self, s):
        def delete_invalid_close(string, open, close):
            new_s = []
            balance = 0
            for c in string:
                if c == open:
                    balance += 1
                if c == close:
                    if balance == 0:
                        continue
                    balance -= 1
                new_s.append(c)
            return "".join(new_s)

        # First pass to remove invalid closing brackets
        s = delete_invalid_close(s, "(", ")")
        # Second pass to remove invalid opening brackets (by reversing the string)
        s = delete_invalid_close(s[::-1], ")", "(")
        # Reverse the string back to original order
        return s[::-1]

    # Approach 2: Using stack and string builder.
    # Time Complexity = O(N)
    # Space Complexity = O(N)
    def minRemoveToMakeValid_2(self, s):
        index_to_remove = set()
        stack = []

        # First pass to find indices of brackets to remove
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif len(stack) == 0:
                index_to_remove.add(i)
            else:
                stack.pop()

        # Add any unmatched opening brackets to the removal set
        index_to_remove = index_to_remove.union(set(stack))
        ans = []

        # Second pass to build the valid string
        for i, c in enumerate(s):
            if i not in index_to_remove:
                ans.append(c)

        return "".join(ans)

# Example usage
X = Solution()
print(X.minRemoveToMakeValid_1("lee(t(c)o)de)"))
print(X.minRemoveToMakeValid_2("lee(t(c)o)de)"))
