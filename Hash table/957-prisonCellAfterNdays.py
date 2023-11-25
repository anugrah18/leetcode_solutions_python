class Solution(object):
    def prisonCellAfterNDays(self,cells,N):
        mem = {}
        fast_forward = False

        while(N>0):
            if(not fast_forward):
                if(tuple(cells) in mem):
                    N = N%(mem[tuple(cells)]-N)
                    fast_forward = True
                else:
                    mem[tuple(cells)]=N
            if(N>0):
                N = N-1
                next_day_cells = self._prisonCellnextDay(cells)
                cells = next_day_cells

        return cells

    def _prisonCellnextDay(self,cells):
        ans = [0]*len(cells)
        ans[0] = ans[len(cells)-1]=0

        for i in range(1, len(cells) - 1):
            if (cells[i - 1] == cells[i + 1]):
                ans[i] = 1
            else:
                ans[i] = 0
        return ans


X = Solution()
print(X.prisonCellAfterNDays([0,1,0,1,1,0,0,1],7))

# Time Complexity : O(N)
# Space Complexity : O(N)