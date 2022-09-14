class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        swap1 = {}
        swap2 = {}

        for ch1, ch2 in zip(s, t):
            if ch1 in swap1.keys():
                if swap1[ch1] != ch2: return False
            else:
                if ch2 in swap2.keys(): return False
                swap1[ch1] = ch2
                swap2[ch2] = ch1
        return True

if __name__ == "__main__":
    s = Solution()
    
    assert s.isIsomorphic('egg', 'add') == True
    assert s.isIsomorphic('foo', 'bar') == False
    assert s.isIsomorphic('paper', 'title') == True
    assert s.isIsomorphic('badc', 'baba') == False

    print('TEST PASSED!')