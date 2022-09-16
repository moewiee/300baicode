class Solution:
    def frequencySort(self, nums: list) -> list:
        d = {}
        for n in nums: d[n] = d[n] + 1 if n in d.keys() else 1
        freq_d = {}
        for k, v in d.items(): freq_d[v] = freq_d[v] + [k] if v in freq_d.keys() else [k]
        
        ret = []
        sorted_freq = sorted(freq_d)
        for freq in sorted_freq:
            instance = sorted(freq_d[freq])[::-1]
            for ins in instance:
                for _ in range(freq):
                    ret.append(ins)
        
        return ret