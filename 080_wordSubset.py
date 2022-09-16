class Solution:
    def wordSubsets(self, words1: list, words2: list) -> list:
        w2_dict = {}
        for word in words2:
            tmp = {}
            for ch in word:
                tmp[ch] = tmp[ch] + 1 if ch in tmp.keys() else 1
            for ch in tmp.keys():
                if ch not in w2_dict.keys():
                    w2_dict[ch] = tmp[ch]
                else:
                    if tmp[ch] > w2_dict[ch]:
                        w2_dict[ch] = tmp[ch]
        
        ret = []
        for word in words1:
            tmp = {}
            for ch in word:
                tmp[ch] = tmp[ch] + 1 if ch in tmp.keys() else 1
            flag = 1
            for ch in w2_dict.keys():
                if ch not in tmp.keys():
                    flag = 0
                else:
                    if w2_dict[ch] > tmp[ch]:
                        flag = 0
            if flag:
                ret.append(word)
        
        return ret
            