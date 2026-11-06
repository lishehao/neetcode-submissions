from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def dfs(index):

            if index == len(s):
                return True

            result = False

            for i in range(len(wordDict)):
                n = len(wordDict[i])
                if s[index: index + n] == wordDict[i]:
                    result = dfs(index + n) or result
                
            return result
        
        return dfs(0)