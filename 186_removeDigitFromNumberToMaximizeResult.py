class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        lastOccurrent = -1
        for i, n in enumerate(number):
            if n == digit:
                if i + 1 < len(number) and number[i+1] > n: return number[:i] + number[i+1:]
                lastOccurrent = i
        return number[:lastOccurrent] + number[lastOccurrent+1:]