class FirstUnique:

    def __init__(self, nums: List[int]):
        self.visited = set()
        self.duplicate = set()
        self.queue = deque()
        for num in nums:
            if num in self.visited:
                self.duplicate.add(num)
            else:
                self.queue.append(num)
            self.visited.add(num)

    def showFirstUnique(self) -> int:
        while self.queue:
            if self.queue[0] not in self.duplicate:
                return self.queue[0]
            else:
                self.queue.popleft()
        return -1

    def add(self, value: int) -> None:
        if value not in self.visited:
            self.queue.append(value)
        else:
            self.duplicate.add(value)
        self.visited.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

'''
visited = 2, 3, 5
duplicate = 5, 2, 3
queue = 5
'''