import re

class Solution:
    def abbrToList(self, abbr):
        abbr = re.split('(\d+)', abbr)
        ret = []
        for i in range(len(abbr)):
            if not abbr[i]:
                pass
            elif abbr[i][0] in ['1','2','3','4','5','6', '7', '8', '9']:
                ret.append(int(abbr[i]))
            elif abbr[i][0] == '0':
                return None
            else:
                for ch in abbr[i]: ret.append(ch)
        
        return ret
    
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr = self.abbrToList(abbr)
        if abbr is None:
            return False
        i = 0
        for value in abbr:
            if isinstance(value, str):
                if i >= len(word):
                    return False
                elif value != word[i]:
                    return False
                i += 1
            else:
                i += value
        
        return i == (len(word))