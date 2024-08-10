class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Initialize pointers for the word and the abbreviation
        word_ptr = abbr_ptr = 0

        # Traverse through both the word and the abbreviation
        while word_ptr < len(word) and abbr_ptr < len(abbr):
            # Check if the current character in the abbreviation is a digit
            if abbr[abbr_ptr].isdigit():
                steps = 0

                # If the abbreviation starts with a '0', it's invalid
                if abbr[abbr_ptr] == "0":
                    return False

                # Calculate the number represented by the digits in the abbreviation
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    steps = steps * 10 + int(abbr[abbr_ptr])
                    abbr_ptr += 1

                # Move the word pointer by the calculated steps (skipping letters)
                word_ptr += steps
            else:
                # If the characters at the current pointers don't match, return False
                if word[word_ptr] != abbr[abbr_ptr]:
                    return False
                # Move both pointers forward
                word_ptr += 1
                abbr_ptr += 1

        # Both pointers should be at the end of their respective strings for a valid abbreviation
        return word_ptr == len(word) and abbr_ptr == len(abbr)


X = Solution()
print(X.validWordAbbreviation("internationalization", "i12iz4n"))  # Expected output: True


# Time Complexity : O(N) , N = length of the word
# Space Complexity : O(1)