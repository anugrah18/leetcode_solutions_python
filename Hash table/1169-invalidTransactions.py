class Solution:
    def invalidTransactions(self,transactions):
        if not transactions:
            return []

        invalid = set()
        past_tran = {}

        for transaction in transactions:
            item = transaction.split(',')
            item[2] = int(item[2])
            item[1] = int(item[1])

            if(item[2]>1000):
                invalid.add(transaction)

            if(item[0] in past_tran):
                for other_transaction in past_tran[item[0]]:
                    other_tran = other_transaction.split(',')
                    other_tran[1] = int(other_tran[1])
                    if(other_tran[3]!=item[3] and abs(item[1]-other_tran[1])<=60):
                        invalid.add(transaction)
                        invalid.add(other_transaction)
                past_tran[item[0]].append(transaction)
            else:
                past_tran[item[0]] = [transaction]

        return list(invalid)


X = Solution()
print(X.invalidTransactions(["alice,20,800,mtv","alice,50,100,beijing"]))

# Time Complexity : O(N)
# Space Complexity : O(N)



