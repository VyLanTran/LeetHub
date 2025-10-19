class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        [1,2],[3,5],[6,7],[8,10],[12,16]
          i

        merge [s1,e1] to [s2, e2]
        if e1 < s2:
            put [s1, e1] to res
            continue to merge [s2, e2] to next intervals
        elif e2 < s1:
            put [s2, e2] to res
            put remaining intervals (from [s1,e1] to the end) into res
        else:
            new_interval = [min(s1, s2), max(e1, e2)]
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