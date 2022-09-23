class Solution:
    def compress(self, chars: list) -> int:
        groupLeft = 0
        groupRight = 0
        writeIdx = 0
        ret = []
        while groupRight < len(chars):
            while groupRight < len(chars) and chars[groupLeft] == chars[groupRight]:
                groupRight += 1
            count = groupRight - groupLeft
            chars[writeIdx] = chars[groupLeft]
            writeIdx += 1
            if count > 1:
                for digit in str(count):
                    chars[writeIdx] = digit
                    writeIdx += 1
            groupLeft = groupRight
        while len(chars) > writeIdx:
            chars.pop()
        