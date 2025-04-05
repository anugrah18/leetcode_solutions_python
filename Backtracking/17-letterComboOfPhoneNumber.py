class Solution:
    def letterCombo(self, digits):
        # Edge case: if the input is empty, return an empty list
        if digits == "":
            return []

        # Mapping of digits to corresponding letters on a phone keypad
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

        res = []  # Final result list to store all letter combinations

        # Recursive backtracking function
        def backtrack(i, curStr):
            # Base case: if the current string has the same length as digits,
            # it means we have a complete combination
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            # Explore all possible characters for the current digit
            for c in dict[digits[i]]:
                # Recurse to the next digit with the current character added
                backtrack(i + 1, curStr + c)

        # Start backtracking from the first digit
        backtrack(0, "")
        return res


# Example usage
X = Solution()
print(X.letterCombo("23"))

# Time Complexity : O(N*4^N)
# Space Complexity : O(N*4^N)
