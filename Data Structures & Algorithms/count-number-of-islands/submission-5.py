from functools import cache
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid[0])
        m = len(grid)

        def dfs(x, y):
            if x < 0 or x == n or y < 0 or y == m:
                return

            if grid[y][x] == "0":
                return
            
            grid[y][x] = "0"
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

        cnt = 0

        for x in range(n):
            for y in range(m):
                if grid[y][x] == "0":
                    continue
                
                cnt += 1
                dfs(x, y)

        return cnt