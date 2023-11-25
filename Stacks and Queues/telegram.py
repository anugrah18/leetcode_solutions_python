"""
Problem : Given a message split it into series of messages with given charlimit without splitting the words. If words get splitted
add it to next message
(Constraint : charlimit>length of longest word in message)
"""
class Solution:
    def telegram(self, message, charLimit):
        temp_text = ""
        temp_word = ""
        ans = []
        queue=message.split(" ")
        while(queue):
            temp_word = queue[0]
            count=len(temp_text)+len(temp_word)
            if count<charLimit:
                temp_text+=temp_word+" "
                queue.pop(0)
            elif count==charLimit:
                temp_text += temp_word
                queue.pop(0)
            else:
                ans.append(temp_text)
                temp_text=""

        if temp_text:
            ans.append(temp_text)
        elif temp_word:
            ans.append(temp_word)

        return ans

X = Solution()
print(X.telegram("This is a sample text. Please go through it. The whole text is'nt that here.",10))
