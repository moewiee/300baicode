class Solution:
    def isValidSudoku(self, board: list) -> bool:
        rows = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        columns = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        blocks = [set(),set(),set(),set(),set(),set(),set(),set(),set()]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.': continue
                if num in rows[i]:
                    return False   
                if num in columns[j]:
                    return False  
                if num in blocks[int(i//3)*3 + int(j//3)]:
                    return False  
                rows[i].add(num)
                columns[j].add(num)
                blocks[int(i//3)*3 + int(j//3)].add(num)
        return True