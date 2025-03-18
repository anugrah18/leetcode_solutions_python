class Solution:
    def addOperators(self, num, target) :

        res = []  # List to store valid expressions

        def dfs(cur_idx, cur_res, cur_sum, prev):
            """
            Performs depth-first search (DFS) to generate expressions by inserting operators.

            Args:
            cur_idx (int): The current index in the num string.
            cur_res (List[str]): The list representing the current expression.
            cur_sum (int): The evaluated sum of the current expression.
            prev (int): The last operand (needed for handling multiplication precedence).
            """
            # Base case: If we have processed the entire string
            if cur_idx >= len(num):
                if cur_sum == target:  # If the computed sum matches the target, add to results
                    res.append("".join(cur_res))  # Convert list to string and store
                return

            # Try forming numbers starting at cur_idx
            for i in range(cur_idx, len(num)):
                cur_str = num[cur_idx:i+1]  # Extract substring as a number
                cur_num = int(cur_str)  # Convert substring to integer

                # If this is the first number, we cannot place an operator before it
                if not cur_res:
                    dfs(i+1, [cur_str], cur_num, cur_num)  # First operand case
                else:
                    # Addition
                    dfs(i+1, cur_res + ["+"] + [cur_str], cur_sum + cur_num, cur_num)

                    # Subtraction
                    dfs(i+1, cur_res + ["-"] + [cur_str], cur_sum - cur_num, -cur_num)

                    # Multiplication (handling precedence)
                    dfs(i+1, cur_res + ["*"] + [cur_str],
                        cur_sum - prev + cur_num * prev, cur_num * prev)

                # Stop early if the number has a leading zero (e.g., "05" is invalid)
                if num[cur_idx] == "0":
                    break

        # Start the DFS search
        dfs(0, [], 0, 0)

        return res  # Return the list of valid expressions

X = Solution()
print(X.addOperators("123",6))

# Time Complexity : O(4^N) , N = digits
# Space Complexity : O(4^N)