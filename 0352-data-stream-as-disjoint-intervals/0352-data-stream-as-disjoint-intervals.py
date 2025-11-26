class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def binary_search(self, value):
        l, r = 0, len(self.intervals) - 1
        while l <= r:
            m = l + (r - l) // 2
            start, end = self.intervals[m]
            if start <= value <= end:
                return m
            elif value < start:
                r = m - 1
            else:
                l = m + 1
        return l
        

    def addNum(self, value: int) -> None:
        n = len(self.intervals)
        if n == 0:
            self.intervals.append([value, value])
            return

        insertion_index = self.binary_search(value)
        print(f'intervals={self.intervals}, value={value}, insertion_index={insertion_index}')
        prev_interval = self.intervals[insertion_index - 1] if insertion_index >= 1 else None
        next_interval = self.intervals[insertion_index] if insertion_index < n else None
        if next_interval is not None and next_interval[0] <= value <= next_interval[-1]:
            return
        elif prev_interval is not None and next_interval is not None and value - 1 == prev_interval[-1] and value + 1 == next_interval[0]:
            self.intervals[insertion_index - 1][-1] = next_interval[-1]
            self.intervals.pop(insertion_index)
        elif prev_interval is not None and value - 1 == prev_interval[-1]:
            self.intervals[insertion_index - 1][-1] = value
        elif next_interval is not None and value + 1 == next_interval[0]:
            self.intervals[insertion_index][0] = value
        else:
            self.intervals.insert(insertion_index, [value, value])
        

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

