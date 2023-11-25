class SparseVector:
    def __init__(self, nums):
        self.nonzeros = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n



    def dotProduct(self, vec) -> int:
        result = 0

        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:
                result += n * vec.nonzeros[i]

        return result

V1 = SparseVector([1,0,0,2,3])
V2 = SparseVector([0,3,0,4,0])
print(V1.dotProduct(V2))

# Time Complexity : O(n)
# Space Complexity : O(m) , m being only non zero elements