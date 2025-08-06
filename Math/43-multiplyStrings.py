class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", the product is "0"
        if "0" in [num1, num2]:
            return "0"

        # Initialize a result array to hold the intermediate results
        # Max possible length of result = len(num1) + len(num2)
        res = [0] * (len(num1) + len(num2))

        # Reverse both numbers to simplify index handling
        num1, num2 = num1[::-1], num2[::-1]

        # Multiply each digit of num1 by each digit of num2
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])  # Multiply digits
                res[i1 + i2] += digit  # Add to the corresponding position

                # Handle carry over to the next position
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10  # Keep only the last digit

        # Reverse result to correct order
        res = res[::-1]

        # Remove leading zeros
        beg = 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # Convert digits to string and join
        res = map(str, res[beg:])
        return "".join(res)

X = Solution()
print(X.multiply("2","3"))

# Time Complexity : O(n × m) , n, m are lengths of num1 and num2
# Space Complexity : O(n+m)