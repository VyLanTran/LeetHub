class KthLargest:
    '''
    Time:
        O(n * log(k)) for initialize initial array 
        O(log(k)) for each addition of a number (including the initial nums)
    Space: O(k)
           
    '''

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heappop(self.min_heap)
            heappush(self.min_heap, val)

        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)