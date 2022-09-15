class Solution:
    def shift_right(self, s:str, amount:int):
        return s[-amount:] + s[:len(s)-amount]
    def shift_left(self, s:str, amount:int):
        return self.shift_right(s, len(s) - amount)
    def stringShift(self, s: str, shift: list) -> str:
        left = 0
        right = 0
        for shift_amount in shift:
            if shift_amount[0]:
                right += shift_amount[1]
            else:
                left += shift_amount[1]
        amount = abs(right - left)
        while amount >= len(s):
            amount = amount - len(s)
        if amount:
            if right > left:
                return self.shift_right(s, amount)
            else:
                return self.shift_left(s, amount)
        else:
            return s
            