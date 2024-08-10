class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = deque()
        if v1:
            self.queue.append((0, v1))
        if v2:
            self.queue.append((0, v2))

    def next(self) -> int:
        i, arr = self.queue.popleft()
        res = arr[i]
        if i + 1 < len(arr):
            self.queue.append((i + 1, arr))
        return res
        

    def hasNext(self) -> bool:
        return self.queue

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())