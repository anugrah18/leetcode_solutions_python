class Solution:
    # Approach 1 Using Stack and string builder.
    # Time Complexity = O(N)
    # Space Complexity = O(N)
    def minRemoveToMakeValid_1(self,s):
        index_to_remove = set()
        stack = []

        for i,c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif len(stack)==0:
                index_to_remove.add(i)
            else:
                stack.pop()

        index_to_remove  = index_to_remove.union(set(stack))
        ans = []
        for i,c in enumerate(s):
            if i not in index_to_remove:
                ans.append(c)

        return "".join(ans)

    # Approach 2 Using two pass string builder.
    # Time Complexity = O(N)
    # Space Complexity = O(N)
    def minRemoveToMakeValid_2(self,s):
        def delete_invalid_close(string,open,close):
            new_s = []
            balance = 0
            for c in string:
                if c == open:
                    balance+=1
                if c == close:
                    if balance ==0:
                        continue
                    balance -=1
                new_s.append(c)
            return "".join(new_s)
        s = delete_invalid_close(s,"(",")")
        s = delete_invalid_close(s[::-1],")","(")
        return s[::-1]


X = Solution()
print(X.minRemoveToMakeValid_1("(a(b(c)d)"))
print(X.minRemoveToMakeValid_2("(a(b(c)d)"))