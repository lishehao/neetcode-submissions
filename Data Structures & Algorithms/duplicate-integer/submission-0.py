from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        for num in cnt:
            if cnt[num] > 1:
                return True

        return False