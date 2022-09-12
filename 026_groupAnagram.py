from string import ascii_lowercase

class Solution:
    def __init__(self):
        self.char_dict = {v:k for k,v in enumerate(ascii_lowercase)}
    
    def getHash(self, s):
        hashstr = [0] * 26
        for ch in s:
            hashstr[self.char_dict[ch]] += 1

        return '.'.join([str(f) for f in hashstr])
        
    def groupAnagrams(self, strs):
        d = {}
        for str in strs:
            hashstr = self.getHash(str)
            if hashstr in d.keys():
                d[hashstr] += [str]
            else:
                d[hashstr] = [str]

        return [v for _,v in d.items()]


if __name__ == "__main__":
    s = Solution()
    # print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # print(s.groupAnagrams([""]))
    # print(s.groupAnagrams(["a"]))
    # print(s.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))
    print(s.getHash("bdddddddddd"))
    print(s.getHash("bbbbbbbbbbc"))