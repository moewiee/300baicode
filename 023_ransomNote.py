class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = {}
        for ch in magazine:
            if ch in m_dict.keys():
                m_dict[ch] += 1
            else:
                m_dict[ch] = 1
                
        for ch in ransomNote:
            if ch not in m_dict.keys():
                return False
            else:
                if m_dict[ch] == 0:
                    return False
                else:
                    m_dict[ch] -= 1
        
        return True
                
        