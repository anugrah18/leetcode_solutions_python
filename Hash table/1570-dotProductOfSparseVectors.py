class SparseVector:
    def __init__(self, nums):
        self.nonzeros = {}  # Dictionary to store index-value pairs of nonzero elements

        # Iterate through nums and store only nonzero values with their indices
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzeros[i] = n  # Store index and value


    def dotProduct(self, vec) -> int:
        result = 0  # Initialize dot product result

        # Iterate through the nonzero elements of the first vector
        for i, n in self.nonzeros.items():
            if i in vec.nonzeros:  # Check if the index exists in the other vector
                result += n * vec.nonzeros[i]  # Multiply values and add to result

        return result  # Return final dot product

V1 = SparseVector([1,0,0,2,3])
V2 = SparseVector([0,3,0,4,0])
print(V1.dotProduct(V2))

# Time Complexity : O(n)
# Space Complexity : O(m) , m being only non zero elements