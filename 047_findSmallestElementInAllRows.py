class Solution:
    def smallestCommonElement(self, mat) -> int:
        d = {}
        m = len(mat)
        n = len(mat[0])
        for row in range(m):
            for col in range(n):
                if mat[row][col] not in d.keys():
                    d[mat[row][col]] = m - 1
                else:
                    d[mat[row][col]] -= 1
                    if d[mat[row][col]] == 0:
                        return mat[row][col]
        
        return -1