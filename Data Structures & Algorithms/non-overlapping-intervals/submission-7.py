class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair: pair[1])
        cnt = 0
        lastSavedInterval = intervals[0]
        for i in range(1, len(intervals)):
            currentInterval = intervals[i]

            if currentInterval[0] < lastSavedInterval[1]:
                cnt += 1
            else:
                lastSavedInterval = currentInterval

        return cnt