class Solution:
    # Approach 1: Using an additional string.
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def compress_1(self, chars):
        ans = ""  # Initialize an empty string to store the compressed characters.
        count = 0  # Initialize a counter to count occurrences of each character.

        for c in chars:
            if len(ans) == 0:
                # If ans is empty, add the first character and reset the count to 1.
                ans += c
                count = 1
            elif ans[-1] == c:
                # If the current character matches the last character in ans, increment the count.
                count += 1
            else:
                # If the current character is different, append the count (if > 1) and the new character.
                if count != 1:
                    ans += str(count)
                ans += c
                count = 1  # Reset the count for the new character.

        # After the loop, append the count for the last set of characters (if > 1).
        if count != 1:
            ans += str(count)

        N = min(len(ans), len(chars))  # Determine the minimum length to avoid exceeding the original array size.

        # Copy the compressed characters from ans back to chars.
        if N == len(ans):
            for i in range(0, N):
                chars[i] = ans[i]
        return N  # Return the length of the compressed string.

    # Approach 2: In-place compression.
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def compress_2(self, chars):
        readIndex = writeIndex = 0  # Initialize two pointers for reading and writing.

        while readIndex < len(chars):
            count = 0  # Initialize a counter to count occurrences of each character.
            letter = chars[readIndex]  # Get the current character.

            # Count the occurrences of the current character.
            while readIndex < len(chars) and chars[readIndex] == letter:
                readIndex += 1
                count += 1

            # Write the character at the writeIndex and increment the writeIndex.
            chars[writeIndex] = letter
            writeIndex += 1

            # If the count is greater than 1, convert the count to a string and write each digit.
            if count > 1:
                for s in str(count):
                    chars[writeIndex] = s
                    writeIndex += 1

        return writeIndex  # Return the length of the compressed string.

# Example usage
X = Solution()
print(X.compress_1(["a","a","b","b","c","c","c"]))
print(X.compress_2(["a","a","b","b","c","c","c"]))
