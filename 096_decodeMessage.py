from string import ascii_lowercase

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        sub = {' ': ' '}
        visited = set()
        i = 0
        for ch in key:
            if ch != ' ':
                if ch not in visited:
                    sub[ch] = ascii_lowercase[i]
                    i += 1
                visited.add(ch)
                
        ret = ''
        for ch in message:
            ret += sub[ch]
        return ret