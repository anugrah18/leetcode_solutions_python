class Solution(object):
    def topKFrequent(self, words, k):
        # Initialize a dictionary to store the frequency of each word
        freq_dict = {}

        # Iterate through each word in the input list
        for word in words:
            # If the word is not already in the dictionary, add it with a count of 1
            if word not in freq_dict:
                freq_dict[word] = 1
            else:
                # If the word exists in the dictionary, increment its count
                freq_dict[word] += 1

        # Create a set of unique words from the dictionary keys
        unique_words = set(freq_dict)

        # Sort the unique words based on two criteria:
        # 1. Descending order of frequency (-freq_dict[x])
        # 2. Alphabetical order of the word (x)
        sorted_words = sorted(unique_words, key=lambda x: (-freq_dict[x], x))

        # Return the top k frequent words from the sorted list
        return sorted_words[:k]


# Create an instance of the Solution class
X = Solution()

# Test the function with a sample input and print the result
print(X.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))

# Time Complexity : O(NLogN)
# - Creating the frequency dictionary takes O(N), where N is the number of words.
# - Sorting the unique words takes O(NLogN) because we sort based on frequency and then alphabetically.

# Space Complexity : O(N)
# - The dictionary stores frequencies for up to N unique words.
