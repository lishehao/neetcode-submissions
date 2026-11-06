class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            interval = intervals[i]

            if interval[1] < newInterval[0]:
                result.append(interval)

            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

            else:
                newInterval = [interval[0] if interval[0] < newInterval[0] else newInterval[0], interval[1] if interval[1] > newInterval[1] else newInterval[1]]
        
        result.append(newInterval)
        return result