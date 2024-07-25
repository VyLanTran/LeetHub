class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        endTime = []
        res, cur = 0, 0
        
        for interval in intervals:
            start, end = interval[0], interval[1]
            while endTime and endTime[0] <= start:
                heappop(endTime)
                cur -= 1
            cur += 1
            res = max(res, cur)
            heappush(endTime, end)
            
        return res
        