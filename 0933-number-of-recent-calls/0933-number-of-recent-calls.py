class RecentCounter:
    # recentCalls

    def __init__(self):
        self.recentCalls = deque()
        

    def ping(self, t: int) -> int:
        while self.recentCalls and t - self.recentCalls[0] > 3000:
            self.recentCalls.popleft()
        self.recentCalls.append(t)
        return len(self.recentCalls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)