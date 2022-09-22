class Solution:
    def findAndReplacePattern(self, words: list, pattern: str) -> list:
        ret = []
        for w in words:
            if len(w) == len(pattern):
                w2p = {}
                p2w = {}
                flag = 1
                for w_ch, p_ch in zip(w, pattern):
                    if w_ch not in w2p: 
                        if p_ch in p2w: 
                            flag = 0
                            break
                        w2p[w_ch] = p_ch
                        p2w[p_ch] = w_ch
                    else:
                        if p_ch not in p2w: 
                            flag = 0
                            break
                        if w2p[w_ch] != p_ch or p2w[p_ch] != w_ch: 
                            flag = 0
                            break
                if flag:
                    ret.append(w)
            
        return ret