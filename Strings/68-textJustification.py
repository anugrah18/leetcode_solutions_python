class Solution:
    def fullJustify(self, words, maxWidth):
        res = []  # Result list to store fully justified lines
        line = []  # Current line being built
        line_length = 0  # Current length of characters in the line

        for word in words:
            # Check if adding this word to the current line will exceed maxWidth
            if line_length + len(line) + len(word) > maxWidth:
                # Calculate the number of spaces to distribute
                extra_space = maxWidth - line_length
                if len(line) == 1:
                    # Special case for a line with only one word
                    # Just pad the end of the single word with spaces
                    res.append(line[0] + ' ' * extra_space)
                else:
                    # Distribute spaces between words
                    spaces = extra_space // (len(line) - 1) # Base number of spaces between words
                    remainder = extra_space % (len(line) - 1) # Extra spaces to distribute
                    # Adding spaces between words
                    for i in range(len(line) - 1):
                        # Add spaces between words, including extra spaces for uneven distribution
                        line[i] += ' ' * (spaces + (1 if i < remainder else 0))
                    res.append(''.join(line))

                # Reset for the next line
                line = []
                line_length = 0

            # Add the current word to the line
            line.append(word)
            line_length += len(word)

        # Handle the last line: left-justified
        last_line = ' '.join(line) # Join words with a single space
        last_line += ' ' * (maxWidth - len(last_line)) # Pad the end of the last line with spaces
        res.append(last_line)

        return res


X = Solution()
print(X.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))


# Time Complexity: O(N), where N is the number of words.
# Space Complexity: O(N), where N is the number of words (for storing the result).



