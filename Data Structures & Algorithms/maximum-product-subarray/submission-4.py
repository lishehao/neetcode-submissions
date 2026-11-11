
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dpMax = [0] * n
        dpMin = [0] * n

        dpMax[0] = nums[0]
        dpMin[0] = nums[0]
        largest = nums[0]

        for i in range(1, n):
            num = nums[i]

            a = num
            b = dpMax[i-1] * num
            c = dpMin[i-1] * num

            dpMax[i] = max(a, b, c)
            dpMin[i] = min(a, b, c)

            largest = max(largest, dpMax[i])

        return largest
