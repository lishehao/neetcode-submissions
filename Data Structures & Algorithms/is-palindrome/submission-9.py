class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            leftC = s[left]
            rightC = s[right]

            if leftC.isalnum() and rightC.isalnum():
                if leftC.lower() == rightC.lower():
                    left += 1
                    right -= 1
                    continue
                
                return False

            if not leftC.isalnum():
                left += 1
            
            if not rightC.isalnum():
                right -= 1

        return True