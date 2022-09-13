class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        char_stack = []
        count_stack = []
        for ch in s:
            if not char_stack:
                char_stack.append(ch)
                count_stack.append(1)
            else:
                if ch == char_stack[-1]:
                    count_stack[-1] += 1
                    if count_stack[-1] == k:
                        count_stack.pop()
                        char_stack.pop()
                else:
                    char_stack.append(ch)
                    count_stack.append(1)
                    
        ret = ''
        for ch, cnt in zip(char_stack, count_stack):
            ret += ch * cnt
        
        return ret