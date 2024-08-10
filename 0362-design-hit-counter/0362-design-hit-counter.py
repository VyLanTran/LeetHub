class HitCounter:

    def __init__(self):
        self.queue = deque()
        self.map = dict()
        self.count = 0
        

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.map:
            self.queue.append(timestamp)
        self.map[timestamp] = self.map.get(timestamp, 0) + 1
        self.count += 1

    def getHits(self, timestamp: int) -> int:
        soonest = max(timestamp - 300 + 1, 1)
        while self.queue and self.queue[0] < soonest:
            t = self.queue.popleft()
            self.count -= self.map[t]
            del self.map[t]
        return self.count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

'''
1, 2, 3, 300
'''