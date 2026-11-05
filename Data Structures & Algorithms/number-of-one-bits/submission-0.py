class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        while True:
            if n == 1:
                return cnt + 1
            
            if n == 0:
                return cnt
            
            if n // 2 != n / 2:
                cnt += 1
            
            n //= 2