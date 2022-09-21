List = list

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ret = ''
        for s in strs:
            if len(s) < 100:
                ret += '0'
            if len(s) < 10:
                ret += '0'
            ret += str(len(s))
            ret += s
        return ret

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ptr = 0
        ret = []
        while ptr < len(s):
            currentStringLen = int(s[ptr:ptr+3])
            ptr += 3
            ret.append(s[ptr:ptr+currentStringLen])
            ptr += currentStringLen
        
        return ret


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))