class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = [character.lower() for character in s if character.isalnum()]

        length = len(cleanS)

        for i in range(length // 2):
            if cleanS[i] == cleanS[length - 1 - i]:
                continue
            
            return False
        
        return True