class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        digits = Counter(num)
        avail = sorted(digits)
        n1, n2 = '', ''
        while avail:
            if len(n1) == len(n2): n1 += avail[0]
            else: n2 += avail[0]
            digits[avail[0]] -= 1
            if digits[avail[0]] == 0: avail.pop(0)
        return int(n1) + int(n2)