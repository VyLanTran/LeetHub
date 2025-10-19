class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        Time: O(n)
        Space: O(1)
        '''

        n = len(intervals)
        res = []
        s1, e1 = newInterval
        i = 0

        while i < n:
            s2, e2 = intervals[i]
            if e1 < s2:
                res.append([s1, e1])
                s1, e1 = s2, e2
            elif e2 < s1:
                res.append([s2, e2])
            else:
                s1, e1 = min(s1, s2), max(e1, e2)
            i += 1

        res.append([s1, e1])
        return res