class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board[0])
        m = len(board)

        def dfs(index, x, y):

            if n <= x or x < 0:
                return False

            if m <= y or y < 0:
                return False

            if word[index] != board[y][x]:
                return False

            if index == len(word) - 1:
                return True

            char = board[y][x]
            board[y][x] = "#"

            result = (
                dfs(index+1, x+1, y)
                or dfs(index+1, x-1, y)
                or dfs(index+1, x, y+1)
                or dfs(index+1, x, y-1)
            )

            board[y][x] = char

            return result

        for i in range(n):
            for j in range(m):
                if dfs(0, i, j):
                    return True

        return False
