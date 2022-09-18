class Solution:
    def evalCurrent(self, s:str):
        s = s.replace('--', '+')

        num, stack, sign = 0, [], "+"
        for ch in s:
            if ch.isdigit(): num = num * 10 + int(ch)
            else:
                if sign == '+': stack.append(num) 
                else: stack.append(-num)
                num, sign = 0, ch
        if sign == '+': stack.append(num) 
        else: stack.append(-num)
        
        return str(sum(stack))
    
    def calculate(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch not in (')', ' '): stack.append(ch) 
            else:
                current = ''
                next_char = ''
                while next_char != '(':
                    next_char = stack.pop()
                    current = next_char + current
                stack.append(self.evalCurrent(current[1:]))
            
        return self.evalCurrent(''.join(stack))