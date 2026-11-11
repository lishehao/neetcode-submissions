class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currentWindow = {}
        largestGlobal = 0

        n = len(s)

        left = 0
        right = 0
        while True:
            if right >= n:
                break

            char = s[right]
            length = right -left + 1
            currentWindow[char] = currentWindow.get(char, 0) + 1

            largest = 0
            for cnt in currentWindow.values():
                largest = max(largest, cnt)
                
            rest = length - largest

            if rest <= k:
                largestGlobal = max(right - left + 1, largestGlobal)
                right += 1
            else:
                currentWindow[s[left]] = currentWindow[s[left]] - 1
                left += 1
                right += 1

        return largestGlobal
            
            
            