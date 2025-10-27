class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # required_rooms = 0
        # pending_end = []
        # intervals.sort()

        # for start, end in intervals:
        #     while len(pending_end) and pending_end[0] <= start:
        #         heapq.heappop(pending_end)
        #     heapq.heappush(pending_end, end)
        #     required_rooms = max(required_rooms, len(pending_end))

        # return required_rooms

        pending_end = []
        intervals.sort()

        for start, end in intervals:
            # we don't need to free up all possible rooms, just need to ask
            # if we can free up 1 room to accommodate current meeting
            if len(pending_end) > 0 and pending_end[0] <= start:
                heapq.heappop(pending_end)
            heapq.heappush(pending_end, end)

        return len(pending_end)