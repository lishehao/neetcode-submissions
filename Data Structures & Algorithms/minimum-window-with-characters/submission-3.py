
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        left = 0
        bestStart = 0
        bestLen = float("inf")

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            while missing == 0:
                length = right - left + 1

                if length < bestLen:
                    bestLen = length
                    bestStart = left

                leftChar = s[left]
                need[leftChar] += 1

                if need[leftChar] > 0:
                    missing += 1

                left += 1

        if bestLen == float("inf"):
            return ""

        return s[bestStart:bestStart + bestLen]
