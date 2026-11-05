class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currentIndex = 0
        nextIndex = 0

        while True:
            if nextIndex >= len(nums) - 1:
                return True

            currentLimit = nums[currentIndex] + currentIndex
            if currentLimit < nums[nextIndex] + nextIndex:
                currentIndex = nextIndex
                nextIndex += 1
                continue

            if nextIndex < currentLimit:
                nextIndex += 1
                continue

            return False