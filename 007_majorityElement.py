class Solution:
    def majorityElement(self, nums) -> int:
        d = {}
        for n in nums:
            if n in d.keys():
                d[n] -= 1
                if d[n] == 0:
                    return n
            else:
                d[n] = int((len(nums) + 1) / 2) - 1
                if d[n] == 0:
                    return n

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))