class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x : x[0])
        cur = intervals[0]
        i = 1
        
        while i < len(intervals):
            next = intervals[i]
            if next[0] <= cur[1]:
                cur = [cur[0], max(cur[1], next[1])]
            else:
                res.append(cur)
                cur = next
            i += 1
        res.append(cur)
        
        return res