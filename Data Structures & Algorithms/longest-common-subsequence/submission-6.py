class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        dp = [[-1] * n2 for _ in range(n1)]

        def dfs(pointer1, pointer2) -> int:
            if pointer1 >= n1 or pointer2 >= n2:
                return 0

            if dp[pointer1][pointer2] != -1:
                return dp[pointer1][pointer2]

            if text1[pointer1] == text2[pointer2]:
                result = dfs(pointer1 + 1, pointer2 + 1) + 1
                dp[pointer1][pointer2] = result
                return result

            result = max(dfs(pointer1 + 1, pointer2), dfs(pointer1, pointer2 + 1))
            dp[pointer1][pointer2] = result
            return result

        return dfs(0,0)