class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Time: O(nlog(n))
        Space: O(n) = space used for sorting
        '''
        res = 0
        intervals.sort(key=lambda x:x[1])
        prev_end = float('-inf')

        for start, end in intervals:
            if start >= prev_end:
                prev_end = end
            else:
                res += 1
        return res