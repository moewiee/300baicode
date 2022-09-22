class SparseVector:
    def __init__(self, nums: list):
        self.v = {}
        
        for i, n in enumerate(nums):
            if n:
                self.v[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.v) > len(vec.v):
            short = vec.v
            long = self.v
        else:
            short = self.v
            long = vec.v
        
        dot = 0
        for i in short:
            dot += short[i] * long[i] if i in long else 0
            
        return dot