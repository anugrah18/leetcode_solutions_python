class Solution:
    def reverseWords(self,s: str) -> str:
        # Initialize variables
        words = []
        word = ""

        # Manually split the string into words
        for char in s:
            if char == " ":
                if word:
                    words.append(word)
                    word = ""
            else:
                word += char

        # Add the last word if there's any
        if word:
            words.append(word)

        # Create an empty list to hold the reversed words
        reversed_words = []

        # Manually reverse the list of words
        for i in range(len(words) - 1, -1, -1):
            reversed_words.append(words[i])

        # Join the reversed list with a single space
        reversed_string = ' '.join(reversed_words)

        return reversed_string

X= Solution()
print(X.reverseWords("    hello    world"))

# Time Complexity = O(N)
# Space Complexity = O(N)
