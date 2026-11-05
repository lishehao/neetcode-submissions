class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency1 = {}
        frequency2 = {}

        for char in s:
            val = frequency1.get(char, 0)
            frequency1[char] = val + 1
        
        for char in t:
            val = frequency2.get(char, 0)
            frequency2[char] = val + 1

        for char, times in frequency1.items():
            if frequency2.get(char, 0) != times:
                return False

        for char, times in frequency2.items():
            if frequency1.get(char, 0) != times:
                return False
            
        return True