class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            if len(self.minHeap) < k:
                heappush(self.minHeap, num)
            elif num > self.minHeap[0]:
                heappop(self.minHeap)
                heappush(self.minHeap, num)
        

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
                heappush(self.minHeap, val)
        elif val > self.minHeap[0]:
            heappop(self.minHeap)
            heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
2, 3, 4,5, 5, 9, 8, 8, 10
'''