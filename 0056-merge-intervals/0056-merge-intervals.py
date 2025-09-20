class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        
        '''

        intervals.sort(key=lambda x: x[0])
        res = []
        last_start, last_end = intervals[0]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if last_end < cur_start:
                res.append([last_start, last_end])
                last_start, last_end = cur_start, cur_end
            else:
                last_end = max(last_end, cur_end)
        
        res.append([last_start, last_end])
        return res
