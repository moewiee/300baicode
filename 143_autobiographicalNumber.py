class Solution:
    def digitCount(self, num: str) -> bool:
        d = {}
        for digit in num:
            d[digit] = d[digit] + 1 if digit in d else 1
        for i in range(len(num)):
            if str(i) in d and int(num[i]) != d[str(i)]:
                return False
            if str(i) not in d and int(num[i]) != 0:
                return False
        return True