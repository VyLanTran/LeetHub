class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        required_rooms = 0
        pending_end = []
        intervals.sort()

        for start, end in intervals:
            while len(pending_end) and pending_end[0] <= start:
                heapq.heappop(pending_end)
            heapq.heappush(pending_end, end)
            required_rooms = max(required_rooms, len(pending_end))

        return required_rooms