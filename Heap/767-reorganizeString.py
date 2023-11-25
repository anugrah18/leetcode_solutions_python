import heapq

class Solution:
    # Approach 1
    # Time Complexity : O(NlogN)
    # Space Complexity : O(2*N)
    def reorganizeString_I(self,s):
        dict = {}
        for c in s:
            dict[c]=dict.get(c,0)-1

        heap = []
        for k in dict:
            heap.append([dict[k],k])
        heapq.heapify(heap)

        prev = None
        res = ""

        while heap or prev:
            if prev and not heap:
                return ""
            # most frequent,except prev
            cnt,chr = heapq.heappop(heap)
            res+=chr
            cnt+=1

            if prev:
                heapq.heappush(heap,prev)
                prev = None
            if cnt!=0:
                prev = [cnt,chr]

        return res

    # Approach 2
    # Time Complexity : O(NlogN)
    # Space Complexity : O(2*N)
    def reorganizeString_II(self,S):

        dict = {}

        for c in S:
            if c not in dict:
                dict[c]=0
            dict[c]-=1

        heap = []
        for k in dict:
            heap.append((dict[k],k))

        heapq.heapify(heap)
        ans = []
        while(len(heap)>=2):
            ncount1,nch1 = heapq.heappop(heap)
            ncount2, nch2 = heapq.heappop(heap)

            ans.extend([nch1,nch2])

            if(ncount1 + 1 !=0):
                heapq.heappush(heap,(ncount1+1,nch1))
            if(ncount2 + 1 != 0):
                heapq.heappush(heap, (ncount2+1, nch2))

        ans = "".join(ans)

        if heap:
            ans = ans+heap[0][1]

        if len(ans) == len(S):
            return ans
        else:
            return ""

X = Solution()
print(X.reorganizeString_I('abbaca'))
print(X.reorganizeString_II('abbaca'))



