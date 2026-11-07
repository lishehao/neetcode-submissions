
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        left = 0
        bestLen = float("inf")
        result = ""

        for right in range(len(s)):
            char = s[right]

            # 扩大窗口
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # 窗口合法，尝试缩小
            while missing == 0:
                if right - left + 1 < bestLen:
                    bestLen = right - left + 1
                    result = s[left:right+1]

                leftChar = s[left]
                need[leftChar] += 1

                if need[leftChar] > 0:
                    missing += 1

                left += 1

        return result
