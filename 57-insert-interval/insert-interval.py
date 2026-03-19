class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        intervals.append(new)
        res = []
        intervals = sorted(intervals, key = lambda x : x[0] )
        i=0
        while i < (len(intervals)):
            interval = [intervals[i][0],intervals[i][1]]
            while i+1<len(intervals) and intervals[i+1][0] <= interval[1]:
                interval[0] = min(intervals[i+1][0],interval[0])
                interval[1] = max(intervals[i+1][1],interval[1])
                print(intervals[i])
                print(intervals[i+1])
                print(interval)
                i+=1
            i+=1
            res.append(interval)
        return res