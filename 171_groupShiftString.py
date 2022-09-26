class Solution:
    def groupStrings(self, strings: list) -> list:
        d = {}
        for subString in strings:
            shiftedString = ''
            for ch in subString:
                shiftedAscii = ord(ch) - (ord(subString[0]) - ord('a'))
                if shiftedAscii >= 97: shiftedString += chr(shiftedAscii)
                else: shiftedString += chr(shiftedAscii + 26)
            if shiftedString in d:
                d[shiftedString].append(subString)
            else:
                d[shiftedString] = [subString]
        
        return [v for k, v in d.items()]
                     