from functools import cache
class Solution:

    def numDecodings(self, s: str) -> int:
        result = 0
        memo = {}

        def dfs(index: int):
            if index == len(s):
                return 1
            
            if int(s[index]) == 0:
                return 0

            if index in memo:
                return memo[index]

            ways = dfs(index + 1)

            if index + 1 < len(s) and 10 <= int(s[index: index + 2]) <= 26:
                ways += dfs(index + 2)

            memo[index] = ways
            return ways

        return dfs(0)