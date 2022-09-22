class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = [0] * 46
        
        s = 0
        x = lowLimit
        while x > 0:
            s += x % 10
            x = x // 10
        boxes[s] += 1
        
        x = lowLimit + 1
        while x <= highLimit:
            if 1 <= x % 10 <= 9:
                s += 1
            else:
                s = 0
                temp = x
                while temp > 0:
                    s += temp % 10
                    temp = temp // 10
            boxes[s] += 1
            x += 1
            
        return max(boxes)