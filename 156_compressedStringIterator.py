from string import ascii_lowercase, ascii_uppercase
from collections import deque

class StringIterator:

    def __init__(self, compressedString: str):
        self.decodedString = self.decodeString(compressedString)
        
    
    def decodeString(self, compressedString):
        letters = []
        repeats = []
        chars = set(ascii_lowercase + ascii_uppercase)
        i = 0
        while i < len(compressedString):
            if compressedString[i] in chars:
                letters.append(compressedString[i])
                i += 1
            else:
                current = ''
                while i < len(compressedString) and compressedString[i] not in chars:
                    current += compressedString[i]
                    i += 1
                current = int(current)
                if current < 200:
                    repeats.append(current)
                else:
                    repeats.append(200)
                    i += 1000
        
        ret = ''
        for l,r in zip(letters, repeats):
            ret += l * r
        
        return deque(ret)

    def next(self) -> str:
        return self.decodedString.popleft() if self.decodedString else ' '
    

    def hasNext(self) -> bool:
        return len(self.decodedString) > 0