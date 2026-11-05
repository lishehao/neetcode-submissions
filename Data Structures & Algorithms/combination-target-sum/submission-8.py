class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        
        def dfs(index: int, prefix: List[int], target: int):

            if target == 0:
                result.append(prefix)
                return

            for i in range(index, len(nums)):

                if nums[i] <= target:
                    newprefix = prefix.copy()
                    newprefix.append(nums[i])

                    dfs(i, newprefix, target - nums[i])

        dfs(0, [], target)

        return result