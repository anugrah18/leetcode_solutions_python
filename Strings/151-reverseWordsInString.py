class Solution:
    def reverseWords(self,s):
        clean_s = []
        temp = ""
        for c in s:
            if c == " ":
                if temp != " ":
                    clean_s.append(temp)
                    temp = ""
            else:
                temp += c

        if temp != "":
            clean_s.append(temp)

        no_space_s = []
        for w in clean_s:
            if w != "":
                no_space_s.append(w)

        return " ".join(no_space_s[::-1])

X= Solution()
print(X.reverseWords("    Hello    World"))

# Time Complexity = O(N)
# Space Complexity = O(N)
