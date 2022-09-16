class Solution:
    def tictactoe(self, moves: list) -> str:
        fill_a = [0] * 8
        fill_b = [0] * 8
        diag_a = [[0,0], [1,1], [2,2]]
        diag_b = [[2,0], [1,1], [0,2]]
        for move in moves[::2]:
            if move in diag_a: fill_a[6] += 1
            if move in diag_b: fill_a[7] += 1
            fill_a[move[0]] += 1
            fill_a[move[1] + 3] += 1
        for move in moves[1::2]:
            if move in diag_a: fill_b[6] += 1
            if move in diag_b: fill_b[7] += 1
            fill_b[move[0]] += 1
            fill_b[move[1] + 3] += 1
        if max(fill_a) == 3:
            return 'A'
        if max(fill_b) == 3:
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'