class Solution:
    def setZeroes(self, matrix) -> None:

        n = len(matrix[0])
        m = len(matrix)

        nTrue = set()
        mTrue = set()

        for x in range(n):
            for y in range(m):
                if matrix[y][x] == 0:
                    nTrue.add(x)
                    mTrue.add(y)

        for x in nTrue:
            for y in range(m):
                matrix[y][x] = 0
        for y in mTrue:
            for x in range(n):
                matrix[y][x] = 0