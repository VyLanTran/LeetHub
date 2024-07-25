class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        endTime = []
        res = 0
        
        # print(intervals)
        
        for interval in intervals:
            start, end = interval[0], interval[1]
            if not endTime or (endTime and endTime[0] > start):
                res += 1
            else:
                heappop(endTime)
            heappush(endTime, end)
            
        return res
        