import copy

class Solution:
    def findCombination(self, nums, target, comb, index, result):
        if target == 0:
            result.append(comb.copy())
            return
        
        for i in range(index, len(nums)):
            if nums[i] <= target:
                newComb = copy.deepcopy(comb)
                newComb.append(nums[i])
                self.findCombination(nums, target - nums[i], newComb, i, result)

        

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = list()
        emptyComb = list()
        self.findCombination(nums, target, emptyComb, 0, result)
        return list(result)