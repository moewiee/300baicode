class ArrayReader:
    def get(self, index: int) -> int:
        pass


class Solution:
    def binary_search(self, reader: 'ArrayReader', low, high, target) -> int:
        mid = int((low + high) / 2)
        while low <= high:
            num = reader.get(mid)
            if num == target:
                return mid
            elif num < target:
                low = mid + 1
                mid = int((low + high) / 2)
            else:
                high = mid - 1
                mid = int((low + high) / 2)
                
        return -1
    
    def search(self, reader: 'ArrayReader', target: int) -> int:
        if reader.get(0) == target:
            return 0

        i = 1
        i_stack = []
        while reader.get(i) <= target:
            i_stack.append(i)
            i *= 2
        if not i_stack:
            return -1 
        low = i_stack[-1]
        
        return self.binary_search(reader, low, low * 2, target)