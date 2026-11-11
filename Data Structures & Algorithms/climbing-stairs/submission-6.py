class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * n 

        dp[0] = 1
        dp[1] = 2
        m = 2
        while m < n:
            dp[m] = dp[m-1] + dp[m-2]
            m += 1

        return dp[n - 1]