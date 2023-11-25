class Solution:
    def letterCombo_I(self,digits):

        if(digits == ""):
            return []

        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in dict[digits[i]]:
                backtrack(i + 1, curStr + c)

        backtrack(0, "")
        return res

    def letterCombo_II(self,digits):

        if(digits == ""):
            return []

        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        output = []
        output.append("")

        for i in range(len(digits)):
            curr = digits[i]
            while(len(output[0])==i):
                perm = output.pop(0)
                for c in dict[curr]:
                    output.append(perm+c)

        return output

X = Solution()
print(X.letterCombo_I("23"))
print(X.letterCombo_II("23"))