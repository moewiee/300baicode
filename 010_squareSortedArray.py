class Solution:
    def sortedSquares(self, nums: list) -> list:
        positive_squares = []
        negative_squares = []
        
        for n in nums:
            if n <= 0:
                negative_squares.append(n ** 2)
            else:
                positive_squares.append(n ** 2)

        i = 0
        j = len(negative_squares) - 1

        ret = []
        while i < len(positive_squares) and j >= 0:
            if positive_squares[i] <= negative_squares[j]:
                ret.append(positive_squares[i])
                i += 1
            else:
                ret.append(negative_squares[j])
                j -= 1
        
        while i < len(positive_squares):
            ret.append(positive_squares[i])
            i += 1
        
        while j >= 0:
            ret.append(negative_squares[j])
            j -= 1

        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))