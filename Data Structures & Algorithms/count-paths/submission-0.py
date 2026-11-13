
from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def find(y, x):
            if y == m -1 and x == n - 1:
                return 1

            if y == m or x == n:
                return 0

            right = find(y, x+1)
            down = find(y+1, x)

            return right + down

        return find(0,0)