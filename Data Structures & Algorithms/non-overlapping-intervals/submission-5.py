class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals, key=lambda x: x[1])

        n = len(sortedIntervals)
        if n == 1:
            return 0

        result = 1
        lastEnd = sortedIntervals[0][1]

        for i in range(1, n):
            if sortedIntervals[i][0] < lastEnd:
                continue
            
            result += 1
            lastEnd = sortedIntervals[i][1]

        return n - result