from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:

        l = len(s)
        
        @cache
        def find(n) -> int:
            if n >= l:
                return 1

            num = int(s[n])
            if num == 0:
                return 0

            a = 0
            if n + 1 < l:
                nextNum = int(s[n+1])
                if 10 <= 10 * num + nextNum <= 26:
                    a = find(n+2)


            b = find(n+1) 

            return a+b

        return find(0)
