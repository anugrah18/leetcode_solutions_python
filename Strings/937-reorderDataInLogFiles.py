class Solution:
    def reorderLogFiles(self,logs):
        return sorted(logs,key=self.get_key)

    def get_key(self,log):
        _id, rest = log.split(" ", maxsplit=1)
        if(rest[0].isalpha()):
            return(0,rest,_id)
        else:
            return(1,)

X = Solution()
print(X.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

# Time Complexity : O(MNLogN) , sorting takes NLogN and comparing two keys will O(M) with N = num of logs and M = max length of logs
# Space Complexity : O(MN)