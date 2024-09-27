class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.overlappings = []

    def doesOverlap(self, start1, end1, start2, end2):
        if end1 <= start2 or end2 <= start1:
            return False
        return True

    def findOverlap(self, start1, end1, start2, end2):
        return (max(start1, start2), min(end1, end2))
        

    def book(self, start: int, end: int) -> bool:
        # print(f"{start, end}, bookings = {self.bookings}, overlappings: {self.overlappings}")
        for curStart, curEnd in self.overlappings:
            if self.doesOverlap(start, end, curStart, curEnd):
                return False
        for curStart, curEnd in self.bookings:
            if self.doesOverlap(start, end, curStart, curEnd):
                self.overlappings.append(self.findOverlap(start, end, curStart, curEnd))
        self.bookings.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)