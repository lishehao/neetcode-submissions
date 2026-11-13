from functools import cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        @cache
        def find(i, j) -> int:
            if i == n1 or j == n2:
                return 0

            if text1[i] == text2[j]:
                return find(i+1, j+1) + 1
            else:
                return max(find(i+1, j), find(i, j+1))

        return find(0,0)