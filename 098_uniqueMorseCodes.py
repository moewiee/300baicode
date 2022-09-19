from string import ascii_lowercase

class Solution:
    def __init__(self):
        self.code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        self.transform = {k: v for k,v in zip(ascii_lowercase, self.code)}
        
    def uniqueMorseRepresentations(self, words: list) -> int:
        s = set()
        for w in words:
            morse = ''.join([self.transform[ch] for ch in w])
            s.add(morse)
        return len(s)