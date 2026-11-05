
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        lastEnd = intervals[0][1]
        removed = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < lastEnd:
                removed += 1
            else:
                lastEnd = intervals[i][1]

        return removed
