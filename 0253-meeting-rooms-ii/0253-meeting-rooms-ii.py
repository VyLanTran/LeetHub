class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        n = len(intervals)
        Time: O(nlog(n))
        Space: O(n)
        '''

        intervals.sort(key = lambda x:x[0])
        required_rooms = 0
        pending = []

        for start, end in intervals:
            while pending and pending[0] <= start:
                heapq.heappop(pending)
            heapq.heappush(pending, end)
            required_rooms = max(required_rooms, len(pending))

        return required_rooms

