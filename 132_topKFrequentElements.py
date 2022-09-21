List = list

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d_n_to_freq = {}
        d_freq_to_n = {}
        for n in nums:
            if n in d_n_to_freq:
                d_n_to_freq[n] += 1
            else:
                d_n_to_freq[n] = 1
            if d_n_to_freq[n] in d_freq_to_n:
                d_freq_to_n[d_n_to_freq[n]].add(n)                
            else:
                d_freq_to_n[d_n_to_freq[n]] = set([n])
            if d_n_to_freq[n] - 1 > 0:
                    d_freq_to_n[d_n_to_freq[n] - 1].remove(n)
        
        d_freq_to_n_keys = sorted(d_freq_to_n)[::-1]
        
        ret = []
        
        for key in d_freq_to_n_keys:
            for element in d_freq_to_n[key]:
                ret.append(element)
                if len(ret) == k: return ret