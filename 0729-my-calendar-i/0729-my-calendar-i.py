class MyCalendar:

    def __init__(self):
        self.events = []
        

    def book(self, start: int, end: int) -> bool:
        i = 0
        while i < len(self.events) and start >= self.events[i][1]:
            i += 1
        if i >= len(self.events) or end <= self.events[i][0]:
            self.events.insert(i, (start, end))
            return True
        return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)