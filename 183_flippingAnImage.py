class Solution:
    def flipAndInvertImage(self, image: list) -> list:
        for row in range(len(image)):
            i = 0
            j = len(image[row]) - 1
            while i <= j:
                if image[row][i] == image[row][j]:
                    image[row][i] = 1 - image[row][i]
                    if i != j: image[row][j] = 1 - image[row][j]
                i += 1
                j -= 1
        return image