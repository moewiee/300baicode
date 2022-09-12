class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        num_pick = {}
        for i, ch in enumerate(s):
            if ch in t:
                if ch in d.keys():
                    d[ch] += [i]
                else:
                    d[ch] = [i]

        for ch in t:
            if ch in num_pick.keys(): num_pick[ch] += 1
            else: num_pick[ch] = 1

        for ch in num_pick.keys():
            if len(d[ch]) < num_pick[ch]:
                return ""
        


if __name__ == "__main__":
    # undone
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
    print(s.minWindow('a', 'aa'))