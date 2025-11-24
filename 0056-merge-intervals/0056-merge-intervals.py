class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        sort by start

        [a, b], [c, d] ==> Assume a <= c 

        if b >= c:
            [a, max(b, d)]
        else:
            append (a, b)
            cur = [c, d]
        '''

        res = []
        intervals.sort(key=lambda x: x[0])
        prev_start, prev_end = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if prev_end < cur_start:
                res.append([prev_start, prev_end])
                prev_start, prev_end = cur_start, cur_end
            else:
                prev_end = max(prev_end, cur_end)
        
        res.append([prev_start, prev_end])
        return res